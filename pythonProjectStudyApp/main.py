# import tkinter as tk
#
# class ELearningApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("E-Learning Platform")
#
#         self.header = tk.Label(self, text="E-Learning Platform", font=("Helvetica", 20))
#         self.header.pack()
#
#         self.keycard_section = tk.Frame(self)
#         self.keycard_section.pack()
#
#         self.keycards = {
#             "Information Technology": ["Keycard 1", "Keycard 2", "Keycard 3"],
#             "Mathematics": ["Keycard A", "Keycard B", "Keycard C"],
#             "Language": ["Keycard X", "Keycard Y", "Keycard Z"]
#         }
#
#         for subject, keycard_list in self.keycards.items():
#             subset_frame = tk.Frame(self.keycard_section)
#             subset_frame.pack()
#
#             tk.Label(subset_frame, text=subject, font=("Helvetica", 16)).pack()
#
#             keycard_items_frame = tk.Frame(subset_frame)
#             keycard_items_frame.pack()
#
#             for keycard in keycard_list:
#                 tk.Label(keycard_items_frame, text=keycard).pack()
#
#         self.timer_section = tk.Frame(self)
#         self.timer_section.pack()
#
#         tk.Label(self.timer_section, text="Timer", font=("Helvetica", 16)).pack()
#
#         self.timer_label = tk.Label(self.timer_section, text="Set Timer (minutes):")
#         self.timer_label.pack()
#
#         self.timer_entry = tk.Entry(self.timer_section)
#         self.timer_entry.pack()
#
#         self.start_exam_button = tk.Button(self.timer_section, text="Start Exam", command=self.start_exam)
#         self.start_exam_button.pack()
#
#         self.timer_display_label = tk.Label(self.timer_section, text="")
#         self.timer_display_label.pack()
#
#         self.footer = tk.Label(self, text="&copy; 2023 E-Learning Platform", font=("Helvetica", 10))
#         self.footer.pack()
#
#     def start_exam(self):
#         timer_value = self.timer_entry.get()
#         if timer_value.isdigit():
#             self.timer_display_label.config(text=f"Exam started! Timer set to {timer_value} minutes.")
#         else:
#             self.timer_display_label.config(text="Invalid timer value. Please enter a valid number of minutes.")
#
# if __name__ == "__main__":
#     app = ELearningApp()
#     app.mainloop()






# import tkinter as tk
# import time
#
# # Create the main GUI window
#
# window=tk.Tk()
# window.title("StudyApp")
# window.geometry("300x200")
#
#
#
# # def examMode():
#
#
#
#
# def countdown(timer):
#     for x in range(timer, -1, -1):
#         seconds = x % 60
#         minutes = (x // 60) % 60
#         hours = x // 3600
#
#         time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
#         timer_label.config(text=time_str)
#         window.update()
#         window.sleep(1)
#     timer_label.config(text="TIME'S UP!")
#
#
# def start_countdown():
#     try:
#         my_time = int(entrytime.get())
#         countdown(my_time)
#     except ValueError:
#         timer_label.config(text="Invalid input")
#
#
# window.title("Countdown Timer")
#
# timer_label = tk.Label(window, text="", font=("Helvetica", 24))
# timer_label.pack()
#
# entrytime = tk.Entry(window)
# entrytime.pack()
#
# start_button = tk.Button(window, text="Start Countdown", command=start_countdown)
# start_button.pack()
#
# # # Create Frames
#
# def math():
#     edtMath=tk.Entry(window,border=10,width=10,bg="black")
#     for i in range(30):
#         edtMath = tk.Entry(window,border=10,width=10,bg="black")
#         edtMath.pack()
#     return edtMath
#
# math=tk.Button(window,text="Math",command=math)
# math.pack()
#
# # Math Flashcards
#
#
# def physics():
#     edtphysics=tk.Entry(window,border=10,width=10,bg="white")
#     for i in range(30):
#         edtphysics = tk.Entry(window,border=10,width=10,bg="white")
#         edtphysics.pack()
#     return edtphysics
#
# physics=tk.Button(window,text="Physics",command=physics)
# physics.pack()
#
# def English():
#     edtEnglish=tk.Entry(window,border=10,width=10,bg="white")
#     for i in range(30):
#         edtEnglish = tk.Entry(window,border=10,width=10,bg="white")
#         edtEnglish.pack()
#     return edtEnglish
#
# English=tk.Button(window,text="English",command=English)
# English.pack()
#
#
#
# # Storing user input
# sName=tk.StringVar()
# sWord=tk.StringVar()
# sDef=tk.StringVar()
#
# # Create the "Create Set" tab and its content
#
#
#
#
# window.mainloop()


import tkinter as tk
import time

def countdown(timer):
    for x in range(timer, -1, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = x // 3600

        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        timer_label.config(text=time_str)
        window.update()
        window.sleep(1)
    timer_label.config(text="TIME'S UP!")


def start_countdown():
    try:
        my_time = int(entrytime.get())
        countdown(my_time)
    except ValueError:
        timer_label.config(text="Invalid input")



def create_flashcards(subject):
    flashcards = []
    for i in range(30):
        entry = tk.Entry(frame, border=10, width=10, bg="white")
        entry.pack()
        flashcards.append(entry)
    return flashcards

window = tk.Tk()
window.title("StudyApp")
window.geometry("400x400")

window.title("Countdown Timer")

timer_label = tk.Label(window, text="", font=("Helvetica", 24))
timer_label.pack()

entrytime = tk.Entry(window)
entrytime.pack()

start_button = tk.Button(window, text="Start Countdown", command=start_countdown)
start_button.pack()

frame = tk.Frame(window)
frame.pack()

math_button = tk.Button(window, text="Math", command=lambda: create_flashcards("Math"))
math_button.pack()

physics_button = tk.Button(window, text="Physics", command=lambda: create_flashcards("Physics"))
physics_button.pack()

english_button = tk.Button(window, text="English", command=lambda: create_flashcards("English"))
english_button.pack()

window.mainloop()
