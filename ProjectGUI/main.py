import tkinter as tk

root = tk.Tk()  # Fixed the capitalization error in 'Tk'

root.geometry("250x250")

# Fixed typo in 'font' parameter and adjusted column position
label = tk.Label(root, text="Python Form", font="Arial 15 bold")
label.grid(row=0, column=2, columnspan=2)  # Using columnspan to center the label

# Fixed variable types and created StringVar instances
namevalue = tk.StringVar()
surnamevalue = tk.StringVar()
phonevalue = tk.StringVar()

# create the text boxes

name = tk.Label(root, text="Name")
surname = tk.Label(root, text="Surname")
phone = tk.Label(root, text="Phone Number")

name.grid(row=1, column=1)  # Adjusted column positions
surname.grid(row=2, column=1)  # Adjusted column positions
phone.grid(row=3, column=1)  # Adjusted column positions

nameentry = tk.Entry(root, textvariable=namevalue)
surnameentry = tk.Entry(root, textvariable=surnamevalue)
phoneentry = tk.Entry(root, textvariable=phonevalue)

nameentry.grid(row=1, column=2)  # Adjusted column positions
surnameentry.grid(row=2, column=2)  # Adjusted column positions
phoneentry.grid(row=3, column=2)  # Adjusted column positions

# Added text to the buttons
button1 = tk.Button(root, text="Add User")
button2 = tk.Button(root, text="Clear Fields")  # Changed the text for the second button

button1.grid(row=4, column=1)  # Adjusted row and column positions
button2.grid(row=4, column=2)  # Adjusted row and column positions

root.mainloop()
