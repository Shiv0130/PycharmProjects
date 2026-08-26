# import random
# import pygame
# import time
#
# MAX_LINES = 3
# MIN_BET = 10
# MAX_BET = 10000
#
# ROWS = 3
# COLS = 3
#
# symbol_count = {
#     "🍒": 2,
#     "🍋": 4,
#     "🍊": 6,
#     "🍉": 8,
# }
#
# symbol_values = {
#     "🍒": 5,
#     "🍋": 4,
#     "🍊": 3,
#     "🍉": 2,
# }
#
# try:
#     pygame.init()
# except pygame.error as e:
#     print("Pygame initialization failed:", e)
#
# # Set up Pygame window
# WIDTH, HEIGHT = 400, 300
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Slot Machine")
#
# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
# # Load symbols
# symbols_images = {
#     "🍒": pygame.image.load("fruit_images/cherry.png"),
#     "🍋": pygame.image.load("fruit_images/lemon.png"),
#     "🍊": pygame.image.load("fruit_images/orange.png"),
#     "🍉": pygame.image.load("fruit_images/watermelon.png")
# }
#
# # Define symbol size and spacing
# SYMBOL_SIZE = 80
# SPACING = 20
#
# # Load background image option 1 (relative path)
# BACKGROUND_1 = pygame.image.load("fruit_images/background.png")
#
# # Load background image option 2 (absolute path)
# BACKGROUND_2 = pygame.image.load("C:/Users/shire/Downloads/background.png")
#
# def deposit():
#     while True:
#         amount = input("HOW MUCH WOULD YOU LIKE TO DEPOSIT? ")
#         if amount.isdigit():
#             amount = int(amount)
#             if amount > 0:
#                 return amount
#             else:
#                 print("AMOUNT MUST BE MORE THAN 0!")
#         else:
#             print("PLEASE ENTER A NUMBER!")
#
# def get_slot_machine_spin(rows, cols, symbols):
#     columns = []
#     for _ in range(cols):
#         column = []
#         for _ in range(rows):
#             symbol = random.choice(list(symbols.keys()))
#             column.append(symbol)
#         columns.append(column)
#     return columns
#
# def draw_window(columns):
#     WIN.blit(BACKGROUND_1, (0, 0))  # Use BACKGROUND_2 for option 2
#     x_offset = (WIDTH - (COLS * (SYMBOL_SIZE + SPACING) - SPACING)) // 2
#     y_offset = (HEIGHT - (ROWS * (SYMBOL_SIZE + SPACING) - SPACING)) // 2
#     for row in range(len(columns[0])):
#         for i, column in enumerate(columns):
#             symbol = column[row]
#             image = symbols_images[symbol]
#             WIN.blit(image, (x_offset + i * (SYMBOL_SIZE + SPACING), y_offset + row * (SYMBOL_SIZE + SPACING)))
#     pygame.display.update()
#
# def spin_animation():
#     spins = 10
#     for _ in range(spins):
#         columns = get_slot_machine_spin(ROWS, COLS, symbol_count)
#         draw_window(columns)
#         time.sleep(0.1)  # Adjust the delay as needed
#
# def main():
#     balance = deposit()
#     while True:
#         print(f"CURRENT BALANCE IS R {balance}")
#         spin_or_quit = input("PRESS ENTER TO PLAY (q to quit).")
#         if spin_or_quit == "q":
#             break
#         spin_animation()
#         # balance = spin(balance)  # You need to implement the spin function to update balance
#
#     pygame.quit()
#
# if _name_ == "_main_":
#     main()


import random
import tkinter as tk

MAX_LINES = 3
MIN_BET = 10
MAX_BET = 10000

ROWS = 3
COLS = 3

symbol_count = {
    "🍒": 2,
    "🍋": 4,
    "🍊": 6,
    "🍉": 8,
}

symbol_values = {
    "🍒": 5,
    "🍋": 4,
    "🍊": 3,
    "🍉": 2,
}

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.balance = 0
        self.bet_amount = 0
        self.create_widgets()

    def create_widgets(self):
        self.balance_label = tk.Label(self.master, text="Balance: $0", font=("Arial", 24))
        self.balance_label.pack()

        self.bet_label = tk.Label(self.master, text="Bet Amount: $0", font=("Arial", 24))
        self.bet_label.pack()

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.bet_entry = tk.Entry(self.master, font=("Arial", 24))
        self.bet_entry.pack()

        self.bet_button = tk.Button(self.master, text="Bet", command=self.bet)
        self.bet_button.pack()

        self.spin_button = tk.Button(self.master, text="Spin", command=self.spin)
        self.spin_button.pack()

        self.result_label = tk.Label(self.master, text="", font=("Arial", 24))
        self.result_label.pack()

    def deposit(self):
        amount = self.bet_entry.get()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                self.balance += amount
                self.balance_label['text'] = f"Balance: ${self.balance}"
            else:
                self.result_label['text'] = "Amount must be more than 0!"
        else:
            self.result_label['text'] = "Please enter a number!"

    def bet(self):
        amount = self.bet_entry.get()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= self.balance:
                self.bet_amount = amount
                self.bet_label['text'] = f"Bet Amount: ${self.bet_amount}"
            else:
                self.result_label['text'] = "Invalid bet amount!"
        else:
            self.result_label['text'] = "Please enter a number!"

    def spin(self):
        columns = self.get_slot_machine_spin(ROWS, COLS, symbol_count)
        result = self.check_win(columns[0])
        if result:
            self.balance += self.bet_amount * 2
            self.balance_label['text'] = f"Balance: ${self.balance}"
            self.result_label['text'] = "Congratulations! You won!"
        else:
            self.balance -= self.bet_amount
            self.balance_label['text'] = f"Balance: ${self.balance}"
            self.result_label['text'] = "Sorry, you lost!"

    def get_slot_machine_spin(self, rows, cols, symbols):
        columns = []
        for _ in range(cols):
            column = []
            for _ in range(rows):
                symbol = random.choice(list(symbols.keys()))
                column.append(symbol)
            columns.append(column)
        return columns

    def check_win(self, row):
        for symbol, count in symbol_count.items():
            if row.count(symbol) == len(row) and count > 1:
                return True
        return False

root = tk.Tk()
root.title("Slot Machine")
my_gui = SlotMachine(root)
root.mainloop()
