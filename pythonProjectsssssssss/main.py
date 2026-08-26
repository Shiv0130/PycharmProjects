# from tkinter import *
# import random
#
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"
#
#
# class Snake:
#
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []
#
#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])
#
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
#             self.squares.append(square)
#
#
# class Food:
#
#     def __init__(self):
#
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#
#         self.coordinates = [x, y]
#
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
#
#
# def next_turn(snake, food):
#
#     x, y = snake.coordinates[0]
#
#     if direction == "up":
#         y -= SPACE_SIZE
#     elif direction == "down":
#         y += SPACE_SIZE
#     elif direction == "left":
#         x -= SPACE_SIZE
#     elif direction == "right":
#         x += SPACE_SIZE
#
#     snake.coordinates.insert(0, (x, y))
#
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#
#     snake.squares.insert(0, square)
#
#     if x == food.coordinates[0] and y == food.coordinates[1]:
#
#         global score
#
#         score += 1
#
#         label.config(text="Score:{}".format(score))
#
#         canvas.delete("food")
#
#         food = Food()
#
#     else:
#
#         del snake.coordinates[-1]
#
#         canvas.delete(snake.squares[-1])
#
#         del snake.squares[-1]
#
#     if check_collisions(snake):
#         game_over()
#
#     else:
#         window.after(SPEED, next_turn, snake, food)
#
#
# def change_direction(new_direction):
#
#     global direction
#
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction
#
#
# def check_collisions(snake):
#
#     x, y = snake.coordinates[0]
#
#     if x < 0 or x >= GAME_WIDTH:
#         return True
#     elif y < 0 or y >= GAME_HEIGHT:
#         return True
#
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             return True
#
#     return False
#
#
# def game_over():
#
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
#                        font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
#
#
# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)
#
# score = 0
# direction = 'down'
#
# label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
# label.pack()
#
# canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()
#
# window.update()
#
# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
#
# x = int((screen_width/2) - (window_width/2))
# y = int((screen_height/2) - (window_height/2))
#
# window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))
#
# snake = Snake()
# food = Food()
#
# next_turn(snake, food)
#
# window.mainloop()


#
# from tkinter import *
# import random
#
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"
#
# class Snake:
#
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []
#
#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])
#
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
#             self.squares.append(square)
#
#
# class Food:
#
#
#     def __init__(self):
#
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#
#         self.coordinates = [x, y]
#
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
#
#
#
# def next_turn(snake, food):
#
#
#
#     x, y = snake.coordinates[0]
#
#     if direction == "up":
#         y -= SPACE_SIZE
#     elif direction == "down":
#         y += SPACE_SIZE
#     elif direction == "left":
#         x -= SPACE_SIZE
#     elif direction == "right":
#         x += SPACE_SIZE
#
#     snake.coordinates.insert(0, (x, y))
#
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#
#     snake.squares.insert(0, square)
#
#     if x == food.coordinates[0] and y == food.coordinates[1]:
#
#         global score
#
#         score += 1
#
#         label.config(text="Score:{}".format(score))
#
#         canvas.delete("food")
#
#         food = Food()
#
#     else:
#
#         del snake.coordinates[-1]
#
#         canvas.delete(snake.squares[-1])
#
#         del snake.squares[-1]
#
#     if check_collisions(snake):
#           game_over()
#
#     else:
#           window.after(SPEED, next_turn, snake, food)
#
#
# def change_direction(new_direction):
#
#     global direction
#
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction
#
#
#
#
# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#
#     if x < 0 or x >= GAME_WIDTH:
#         return True
#     elif y < 0 or y >= GAME_HEIGHT:
#         return True
#
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             return True
#
#     return False
#
#
#
#
# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
#                        font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
#
# def start_new_game():
#     global snake, food, score, direction
#     canvas.delete(ALL)
#     score = 0
#     direction = 'down'
#     label.config(text="Score:{}".format(score))
#     snake = Snake()
#     food = Food()
#     next_turn(snake, food)
#
# def pause_game():
#     canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
#                        font=('consolas', 40), text="PAUSED", fill="white", tag="pause")
#     canvas.after_cancel(next_turn_id)
#
# def resume_game():
#     canvas.delete("pause")
#     next_turn(snake, food)
#
# def restart_game():
#     canvas.delete(ALL)
#     start_new_game()
#
# def quit_game():
#     canvas.delete(ALL)
#     label.config(text="Score: 0")
#     canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
#                        font=('consolas', 40), text="MAIN SCREEN", fill="white", tag="mainscreen")
#
# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)
#
# score = 0
# direction = 'down'
#
# label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
# label.pack()
#
# canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()
#
# window.update()
#
# # ... (unchanged)
#
# start_button = Button(window, text="New Game", command=start_new_game)
# start_button.pack()
#
# continue_button = Button(window, text="Continue", command=resume_game)
# continue_button.pack()
#
# quit_button = Button(window, text="Quit", command=quit_game)
# quit_button.pack()
#
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))
#
# snake = Snake()
# food = Food()
#
# next_turn_id = next_turn(snake, food)
#
# window.mainloop()

# from tkinter import *
# import random
#
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"
#
# class Snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []
#
#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])
#
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
#             self.squares.append(square)
#
# class Food:
#     def __init__(self):
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#         self.coordinates = [x, y]
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
#
# def next_turn(snake, food):
#     x, y = snake.coordinates[0]
#
#     if direction == "up":
#         y -= SPACE_SIZE
#     elif direction == "down":
#         y += SPACE_SIZE
#     elif direction == "left":
#         x -= SPACE_SIZE
#     elif direction == "right":
#         x += SPACE_SIZE
#
#     snake.coordinates.insert(0, (x, y))
#
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#     snake.squares.insert(0, square)
#
#     if x == food.coordinates[0] and y == food.coordinates[1]:
#         global score
#         score += 1
#         label.config(text="Score:{}".format(score))
#         canvas.delete("food")
#         food = Food()
#     else:
#         del snake.coordinates[-1]
#         canvas.delete(snake.squares[-1])
#         del snake.squares[-1]
#
#     if check_collisions(snake):
#         game_over()
#     else:
#         window.after(SPEED, next_turn, snake, food)
#
# def change_direction(new_direction):
#     global direction
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction
#
# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#
#     if x < 0:
#         snake.coordinates[0] = (GAME_WIDTH - SPACE_SIZE, y)
#     elif x >= GAME_WIDTH:
#         snake.coordinates[0] = (0, y)
#
#     if y < 0:
#         snake.coordinates[0] = (x, GAME_HEIGHT - SPACE_SIZE)
#     elif y >= GAME_HEIGHT:
#         snake.coordinates[0] = (x, 0)
#
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             return True
#
#     return False
#
# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
#                        font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
#     start_button.pack()
#     restart_button.pack()
#     quit_button.pack()
#
# def open_pause_menu():
#     pause_menu = Toplevel(window)
#     pause_menu.title("Pause Menu")
#
#     resume_button = Button(pause_menu, text="Resume", command=resume_game)
#     resume_button.pack()
#
#     restart_button = Button(pause_menu, text="Restart", command=restart_game)
#     restart_button.pack()
#
#     quit_button = Button(pause_menu, text="Quit", command=quit_game)
#     quit_button.pack()
#
# def resume_game():
#     canvas.delete("pause")
#     window.after(SPEED, next_turn, snake, food)
#
# def restart_game():
#     canvas.delete(ALL)
#     start_new_game()
#
# def quit_game():
#     window.destroy()
#
# def start_new_game():
#     global snake, food, score, direction
#     canvas.delete(ALL)
#     score = 0
#     direction = 'down'
#     label.config(text="Score:{}".format(score))
#     snake = Snake()
#     food = Food()
#     next_turn(snake, food)
#
# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)
#
# score = 0
# direction = 'down'
#
# label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
# label.pack()
#
# canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()
#
# start_button = Button(window, text="New Game", command=start_new_game)
# restart_button = Button(window, text="Restart", command=restart_game)
# quit_button = Button(window, text="Quit", command=quit_game)
#
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))
# window.bind('<Escape>', lambda event: open_pause_menu())
#
# snake = Snake()
# food = Food()
#
# next_turn(snake, food)
#
# window.mainloop()
#
#
#
#
#
#
#
#
# from tkinter import *
# import random
#
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"
#
# class Snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []
#
#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])
#
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
#             self.squares.append(square)
#
# class Food:
#     def __init__(self):
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#         self.coordinates = [x, y]
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
#
# def next_turn(snake, food):
#     x, y = snake.coordinates[0]
#
#     if direction == "up":
#         y -= SPACE_SIZE
#     elif direction == "down":
#         y += SPACE_SIZE
#     elif direction == "left":
#         x -= SPACE_SIZE
#     elif direction == "right":
#         x += SPACE_SIZE
#
#     snake.coordinates.insert(0, (x, y))
#
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#     snake.squares.insert(0, square)
#
#     if x == food.coordinates[0] and y == food.coordinates[1]:
#         global score
#         score += 1
#         label.config(text="Score:{}".format(score))
#         canvas.delete("food")
#         food = Food()
#     else:
#         del snake.coordinates[-1]
#         canvas.delete(snake.squares[-1])
#         del snake.squares[-1]
#
#     if check_collisions(snake):
#         game_over()
#     else:
#         window.after(SPEED, next_turn, snake, food)
#
# def change_direction(new_direction):
#     global direction
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction
#
# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#
#     if x < 0:
#         snake.coordinates[0] = (GAME_WIDTH - SPACE_SIZE, y)
#     elif x >= GAME_WIDTH:
#         snake.coordinates[0] = (0, y)
#
#     if y < 0:
#         snake.coordinates[0] = (x, GAME_HEIGHT - SPACE_SIZE)
#     elif y >= GAME_HEIGHT:
#         snake.coordinates[0] = (x, 0)
#
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             return True
#
#     return False
#
# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
#                        font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
#     start_button.pack()
#     quit_button.pack()
#
# def open_pause_menu():
#     global next_turn_id
#     canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
#                        font=('consolas', 40), text="PAUSED", fill="white", tag="pause")
#     canvas.after_cancel(next_turn_id)
#
#     pause_menu = Toplevel(window)
#     pause_menu.title("Pause Menu")
#
#     resume_button = Button(pause_menu, text="Resume", command=resume_game)
#     resume_button.pack()
#
#     restart_button = Button(pause_menu, text="Restart", command=restart_game)
#     restart_button.pack()
#
#     quit_button = Button(pause_menu, text="Quit", command=quit_game)
#     quit_button.pack()
#
# def resume_game():
#     global next_turn_id
#     canvas.delete("pause")
#     next_turn_id = window.after(SPEED, next_turn, snake, food)
#
# def restart_game():
#     global snake, food, score, direction, next_turn_id
#     canvas.delete(ALL)
#     score = 0
#     direction = 'down'
#     label.config(text="Score:{}".format(score))
#     snake = Snake()
#     food = Food()
#     next_turn_id = window.after(SPEED, next_turn, snake, food)
#
# def quit_game():
#     window.destroy()
#
# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)
#
# score = 0
# direction = 'down'
# next_turn_id = None
#
# label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
# label.pack()
#
# canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()
#
# start_button = Button(window, text="New Game", command=restart_game)
# quit_button = Button(window, text="Quit", command=quit_game)
#
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))
# window.bind('<Escape>', lambda event: open_pause_menu())
#
# snake = Snake()
# food = Food()
#
# next_turn_id = window.after(SPEED, next_turn, snake, food)
#
# window.mainloop()



from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#3776ab"
FOOD_COLOR = "#FFd343"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0:
        snake.coordinates[0] = (GAME_WIDTH - SPACE_SIZE, y)
    elif x >= GAME_WIDTH:
        snake.coordinates[0] = (0, y)

    if y < 0:
        snake.coordinates[0] = (x, GAME_HEIGHT - SPACE_SIZE)
    elif y >= GAME_HEIGHT:
        snake.coordinates[0] = (x, 0)

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    start_button.pack()
    quit_button.pack()

def open_pause_menu():
    global next_turn_id
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 40), text="PAUSED", fill="white", tag="pause")
    canvas.after_cancel(next_turn_id)

    pause_menu = Toplevel(window)
    pause_menu.title("Pause Menu")

    resume_button = Button(pause_menu, text="Resume", command=resume_game)
    resume_button.pack()

    new_game_button = Button(pause_menu, text="New Game", command=restart_game)
    new_game_button.pack()

    quit_button = Button(pause_menu, text="Quit", command=quit_game)
    quit_button.pack()

def resume_game():
    global next_turn_id
    canvas.delete("pause")
    next_turn_id = window.after(SPEED, next_turn, snake, food)

def restart_game():
    global snake, food, score, direction, next_turn_id
    canvas.delete(ALL)
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    snake = Snake()
    food = Food()
    next_turn_id = window.after(SPEED, next_turn, snake, food)

def quit_game():
    window.destroy()

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'
next_turn_id = None

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

start_button = Button(window, text="New Game", command=restart_game)
quit_button = Button(window, text="Quit", command=quit_game)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Escape>', lambda event: open_pause_menu())

snake = Snake()
food = Food()

next_turn_id = window.after(SPEED, next_turn, snake, food)

window.mainloop()

