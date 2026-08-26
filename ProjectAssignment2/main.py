import tkinter as tk

# Function to display name and address
def display_info():
    # Hardcoding name and address for demonstration purposes
    name = "Mr Sewnarain"
    address = "7 Morningstar street"

    # Update the text of the info_label with name and address
    lblInfo.config(text=f"Name: {name}\nAddress: {address}")

# Function to close the tkinter window
def quit_app():
    window.destroy()

# Create the main window
window = tk.Tk()

# Set the title and dimensions of the main window
window.title("Name and Address")
window.geometry("300x200")

# Create a label widget to display info
lblInfo = tk.Label(window, text="", padx=20, pady=20)
lblInfo.pack()

# Create a button widget to trigger the display_info function
btnShowInfo = tk.Button(window, text="Show Info", command=display_info)
btnQuit = tk.Button(window, text="Quit", command=quit_app)  # Assign the quit_app function
btnShowInfo.pack(side="left")
btnQuit.pack(side="right")

# Start the GUI event loop
window.mainloop()


import tkinter as tk


# Function to calculate and display the average
def calc_avg():
    # Get test scores from the Entry widgets and convert them to float
    mark1 = float(entry1.get())
    mark2 = float(entry2.get())
    mark3 = float(entry3.get())

    # Calculate the average
    avg = (mark1 + mark2 + mark3) / 3

    # Update the label with the calculated average
    lblResult.config(text=f"Average marks are{avg:.2f}")

# Function to close the tkinter window
def quit_app():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Test Score Average Calculator")
window.geometry("300x200")

# Create Entry widgets for test scores
entry1 = tk.Entry(window,width=10)
entry2 = tk.Entry(window,width=10)
entry3 = tk.Entry(window,width=10)

entry1.pack()
entry2.pack()
entry3.pack()

# Create a button to calculate the average
btnCalc = tk.Button(window,text="Calculate Average:",command=calc_avg)
btnQuit = tk.Button(window, text="Quit", command=quit_app)  # Assign the quit_app function
btnCalc.pack()
btnQuit.pack()
# Create a label to display the result
lblResult=tk.Label(window,text="", pady=10)
lblResult.pack()

# Start the GUI event loop
window.mainloop()



