# # Tkinter with databases
#
# # Using tkinter with an interface of a button and a couple of entry components
# # I want the program to let me enter the data using tkinter components and after I enter the data it puts the information  into a database using sqilte3
# # It then reads the database in the console.Is this the right way of doing it?
#
# import tkinter as tk
# import sqlite3
#
# window = tk.Tk()
#
# window.title("Tk with DB")
#
# window.geometry("300x200")
#
# def addtoDatabase():
#     conn=sqlite3.connect("address_book.db")
#     c=conn.cursor()
#     first_name=entry1.get()
#     last_name=entry2.get()
#     address=entry3.get()
#     zipcode=int(entry4.get())
#
#
#     c.execute("Create TABLE IF NOT EXISTS address(first_name text,last_name text,address text,city text,zipcode integer) ")
#     c.execute("INSERT INTO address(first_name,last_name,address,city,zipcode) Values(?,?,?,?)",first_name,last_name,address,zipcode)
#     c.execute("select* from address_book")
#     results=c.fetchall()
#     print("\naddreeses of all:")
#     for row in results:
#         print("Name:", row[0])
#         print("Surname:", row[1])
#         print("Address:", row[2])
#         print("Zip code", row[3])
#     conn.commit()
#     conn.close()
#
#     label.config("Information has been addded to the database")
#
# entry1=tk.Entry(window,width= 10)
#
# entry1.pack()
#
# entry2=tk.Entry(window,width= 10)
#
# entry2.pack()
#
# entry3=tk.Entry(window,width= 10)
#
# entry3.pack()
#
# entry4=tk.Entry(window,width= 10)
#
# entry4.pack()
#
# label=tk.Label(window,text=" ")
# label.pack()
#
#
# button=tk.Button(window,text="Add to database",command=addtoDatabase)
#
#
# window.mainloop()




import tkinter as tk
import sqlite3

window = tk.Tk()

window.title("Tk with DB")

window.geometry("400x200")

def addtoDatabase():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    first_name = entry1.get()
    last_name = entry2.get()
    address = entry3.get()
    zipcode = int(entry4.get())

    c.execute("CREATE TABLE IF NOT EXISTS address(first_name text,last_name text,address text,zipcode integer)")
    c.execute("INSERT INTO address(first_name,last_name,address,zipcode) VALUES(?,?,?,?)", (first_name, last_name, address, zipcode))
    c.execute("SELECT * FROM address")
    results = c.fetchall()
    print("\nAddresses of all:")
    for row in results:
        print("Name:", row[0])
        print("Surname:", row[1])
        print("Address:", row[2])
        print("Zip code", row[3])
    conn.commit()
    conn.close()

    label.config(text="Information has been added to the database")

# Labels
label1 = tk.Label(window, text="First Name:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

label2 = tk.Label(window, text="Last Name:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

label3 = tk.Label(window, text="Address:")
label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

label4 = tk.Label(window, text="Zipcode:")
label4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

# Entry widgets
entry1 = tk.Entry(window, width=20)
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2 = tk.Entry(window, width=20)
entry2.grid(row=1, column=1, padx=10, pady=5)

entry3 = tk.Entry(window, width=20)
entry3.grid(row=2, column=1, padx=10, pady=5)

entry4 = tk.Entry(window, width=20)
entry4.grid(row=3, column=1, padx=10, pady=5)

label = tk.Label(window, text=" ")
label.grid(row=4, column=0, columnspan=2, pady=10)

button = tk.Button(window, text="Add to database", command=addtoDatabase)
button.grid(row=5, column=0, columnspan=2)

window.mainloop()

