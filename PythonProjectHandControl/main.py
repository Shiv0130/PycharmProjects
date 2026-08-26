"""
╔══════════════════════════════════════════════════════╗
║           HAND GESTURE MOUSE CONTROLLER              ║
║                                                      ║
║  INSTALL DEPENDENCIES FIRST — run this in terminal:  ║
║  pip install mediapipe opencv-python pyautogui numpy ║
║                                                      ║
║  In PyCharm: Open Terminal (bottom bar) and paste    ║
║  the pip install line above, then hit Enter.         ║
╚══════════════════════════════════════════════════════╝

GESTURES:
  ✋ Index finger up alone     → Move your mouse cursor
  🤌 Index + Thumb pinch       → Click (release to drop)
  🤏 Middle + Thumb pinch      → Double-click (open file)
  ✊ Fist (all fingers closed)  → Pause tracking

HOW TO QUIT:
  Press Q on the webcam window to exit.
"""

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# ─────────────────────────────────────────────
#  SETTINGS  (tweak these if needed)
# ─────────────────────────────────────────────
CAMERA_INDEX      = 0      # Try 1 or 2 if wrong camera opens
SMOOTHING         = 6      # 1 = raw/fast, 10 = very smooth/slow
PINCH_THRESHOLD   = 0.05   # How close fingers must be to count as pinch
CLICK_COOLDOWN    = 0.4    # Seconds to wait between clicks (avoids spam)
FRAME_MARGIN      = 100    # Dead-zone margin in pixels from webcam edge
# ─────────────────────────────────────────────

# PyAutoGUI safety — moves mouse to corner to abort if things go wrong
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0        # No extra delay between pyautogui calls

# Screen resolution
SCREEN_W, SCREEN_H = pyautogui.size()

# MediaPipe hands setup
mp_hands   = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands      = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,          # Track only one hand
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)

# Webcam
cap = cv2.VideoCapture(CAMERA_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

CAM_W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
CAM_H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Smoothing buffer — stores last N cursor positions and averages them
smooth_x_buffer = []
smooth_y_buffer = []

# Click state tracking
last_click_time     = 0
index_pinch_held    = False   # True while index+thumb are pinched (for drag)


# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_landmark(landmarks, index):
    """Return (x, y) for a given landmark index, in pixel coords."""
    lm = landmarks[index]
    return lm.x, lm.y   # Normalized 0.0 to 1.0


def pinch_distance(landmarks, finger_tip_index, thumb_tip_index=4):
    """
    Calculate the Euclidean distance between two fingertips.
    Returns a ratio (0.0 to ~0.3) relative to hand size.
    We normalize by wrist-to-middle-finger distance so it works
    at any distance from the camera.
    """
    fx, fy = get_landmark(landmarks, finger_tip_index)
    tx, ty = get_landmark(landmarks, thumb_tip_index)

    # Hand size reference: wrist (0) to middle finger MCP (9)
    wx, wy = get_landmark(landmarks, 0)
    mx, my = get_landmark(landmarks, 9)
    hand_size = np.hypot(mx - wx, my - wy) + 1e-6  # avoid divide by zero

    dist = np.hypot(fx - tx, fy - ty)
    return dist / hand_size


def is_finger_extended(landmarks, tip, pip):
    """
    Returns True if a finger is extended (tip is above pip joint).
    Uses Y axis — in MediaPipe, smaller Y = higher on screen.
    """
    tip_y = landmarks[tip].y
    pip_y = landmarks[pip].y
    return tip_y < pip_y


def smooth_cursor(new_x, new_y):
    """
    Smooth cursor movement using a rolling average buffer.
    Prevents jittery movement from small hand trembles.
    """
    smooth_x_buffer.append(new_x)
    smooth_y_buffer.append(new_y)

    if len(smooth_x_buffer) > SMOOTHING:
        smooth_x_buffer.pop(0)
        smooth_y_buffer.pop(0)

    return int(np.mean(smooth_x_buffer)), int(np.mean(smooth_y_buffer))


def map_to_screen(norm_x, norm_y):
    """
    Map a normalized webcam coordinate (0.0–1.0) to screen coordinates.
    FRAME_MARGIN crops the edges so you don't need to move your hand
    all the way to the camera edge to reach screen edges.
    """
    # Clamp to usable area
    usable_x = np.clip(norm_x, FRAME_MARGIN / CAM_W, 1 - FRAME_MARGIN / CAM_W)
    usable_y = np.clip(norm_y, FRAME_MARGIN / CAM_H, 1 - FRAME_MARGIN / CAM_H)

    # Remap to 0.0–1.0 within usable area
    mapped_x = (usable_x - FRAME_MARGIN / CAM_W) / (1 - 2 * FRAME_MARGIN / CAM_W)
    mapped_y = (usable_y - FRAME_MARGIN / CAM_H) / (1 - 2 * FRAME_MARGIN / CAM_H)

    # Flip X because webcam is mirrored
    mapped_x = 1 - mapped_x

    return int(mapped_x * SCREEN_W), int(mapped_y * SCREEN_H)


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────

print("\n🖐  Hand Mouse Controller running!")
print("   Move your index finger to move the cursor.")
print("   Pinch index+thumb to click/drag.")
print("   Pinch middle+thumb to double-click.")
print("   Press Q in the webcam window to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Could not read from webcam. Check CAMERA_INDEX setting.")
        break

    # Flip frame horizontally so it acts like a mirror (more natural)
    frame = cv2.flip(frame, 1)

    # Convert BGR (OpenCV) to RGB (MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results   = hands.process(rgb_frame)

    # Default status shown on screen
    status_text  = "No hand detected"
    status_color = (100, 100, 100)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        lm             = hand_landmarks.landmark

        # Draw hand skeleton on the webcam preview
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # ── Finger extension checks ──────────────────────────
        # Landmark indices: tip / pip (joint below tip)
        # Index=8/6, Middle=12/10, Ring=16/14, Pinky=20/18, Thumb=4/3
        index_up  = is_finger_extended(lm, 8, 6)
        middle_up = is_finger_extended(lm, 12, 10)
        ring_up   = is_finger_extended(lm, 16, 14)
        pinky_up  = is_finger_extended(lm, 20, 18)

        # ── Pinch distance checks ────────────────────────────
        index_pinch_dist  = pinch_distance(lm, 8,  4)   # Index tip + Thumb tip
        middle_pinch_dist = pinch_distance(lm, 12, 4)   # Middle tip + Thumb tip

        index_pinching  = index_pinch_dist  < PINCH_THRESHOLD
        middle_pinching = middle_pinch_dist < PINCH_THRESHOLD

        # ── Fist detection (pause) ───────────────────────────
        is_fist = not index_up and not middle_up and not ring_up and not pinky_up

        # ── Cursor position = index fingertip ────────────────
        ix, iy       = get_landmark(lm, 8)
        screen_x, screen_y = map_to_screen(ix, iy)
        smooth_x, smooth_y = smooth_cursor(screen_x, screen_y)

        now = time.time()

        # ── GESTURE LOGIC ────────────────────────────────────

        if is_fist:
            # ✊ Fist — pause everything
            status_text  = "PAUSED (fist)"
            status_color = (0, 165, 255)
            smooth_x_buffer.clear()
            smooth_y_buffer.clear()

        elif middle_pinching and (now - last_click_time) > CLICK_COOLDOWN:
            # 🤏 Middle + Thumb → Double click
            pyautogui.doubleClick(smooth_x, smooth_y)
            last_click_time = now
            status_text  = "DOUBLE CLICK (open)"
            status_color = (0, 0, 255)
            print(f"  🖱  Double-click at ({smooth_x}, {smooth_y})")

        elif index_pinching:
            # 🤌 Index + Thumb → Click / Drag
            if not index_pinch_held:
                pyautogui.mouseDown(smooth_x, smooth_y)
                index_pinch_held = True
                last_click_time  = now
                print(f"  🖱  Click/drag start at ({smooth_x}, {smooth_y})")
            else:
                pyautogui.moveTo(smooth_x, smooth_y)
            status_text  = "CLICK / DRAGGING"
            status_color = (0, 255, 0)

        else:
            # ✋ Default — just move cursor
            if index_pinch_held:
                # Released pinch — mouse up
                pyautogui.mouseUp()
                index_pinch_held = False
                print(f"  🖱  Released at ({smooth_x}, {smooth_y})")

            pyautogui.moveTo(smooth_x, smooth_y)
            status_text  = "MOVING"
            status_color = (255, 200, 0)

        # ── Draw index fingertip dot on preview ──────────────
        tip_px = int(ix * CAM_W), int(iy * CAM_H)
        cv2.circle(frame, tip_px, 12, status_color, -1)
        cv2.circle(frame, tip_px, 14, (255, 255, 255), 2)

        # ── Draw pinch distance indicators ───────────────────
        # Index pinch bar
        bar_len = int((1 - min(index_pinch_dist / PINCH_THRESHOLD, 1)) * 100)
        cv2.rectangle(frame, (10, 60), (10 + bar_len, 75), (0, 255, 100), -1)
        cv2.putText(frame, "Index pinch", (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

        # Middle pinch bar
        bar_len2 = int((1 - min(middle_pinch_dist / PINCH_THRESHOLD, 1)) * 100)
        cv2.rectangle(frame, (10, 95), (10 + bar_len2, 110), (0, 100, 255), -1)
        cv2.putText(frame, "Middle pinch", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

    # ── HUD overlay ──────────────────────────────────────────
    cv2.rectangle(frame, (0, 0), (CAM_W, 40), (30, 30, 30), -1)
    cv2.putText(frame, f"STATUS: {status_text}", (10, 27),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, status_color, 2)
    cv2.putText(frame, "Q = quit", (CAM_W - 90, 27),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)

    cv2.imshow("Hand Mouse Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ── Cleanup ───────────────────────────────────────────────
cap.release()
cv2.destroyAllWindows()
hands.close()
print("\n👋 Hand Mouse Controller closed.")