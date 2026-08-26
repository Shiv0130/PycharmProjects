# Inheritance
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Polymorphism
def add(x, y):
    return x + y

result1 = add(5, 10)          # Sum of integers
result2 = add("Hello", "World")  # Concatenation of strings

# class Person:
#     def __init__(self,age,name):
#         self.name=name
#         self.age=age
#
#
#     def details(self):
#         print(self.name)
#         print(self.age)
#
# namee=input("Enter your name:")
# agee=input("Enter your age:")
#
# People1=Person(agee,namee)
#
# People2=People1.details()
#
# print(People2)

#
class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

# Example usage
name_input = input("Enter your name:")
age_input = int(input("Enter your age:"))

people1 = Person(age_input, name_input)

# Get and print details
print("Initial details:")
print("Name:", people1.get_name())
print("Age:", people1.get_age())

# Update and print details
new_name_input = input("Enter updated name:")
new_age_input = int(input("Enter updated age:"))

people1.set_name(new_name_input)
people1.set_age(new_age_input)

print("\nUpdated details:")
print("Name:", people1.get_name())
print("Age:", people1.get_age())

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Encapsulation
class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

#
#
# # List=[20,30,40,
# #       50,60,70,80,
# #       90,100,110,120]
# #
# # def element():
# #     for i in range(len(List)):
# #         for j in range(len(List[i])):
# #
# #             print(i*j)
# # element()
# #
#
#
#
# # def create_list(rows,cols):
# #     List=[]
# #
# #     for rows in range(rows):
# #         List_row=[]
# #         for cols in range(cols):
# #             values=int(input("Enter a value:"))
# #             List_row.append(values)
# #             List.append(List_row)
# #
# #             return List
# #
# # rowss=int(input("Enter the rows:"))
# # colls=int(input("Enter the cols:"))
# #
# # create_list(rowss,colls)
# #
# # print("The elements in the list are:",create_list(rowss,colls))
#
def create_2d_array(rows, cols):
    array = []
    for _ in range(rows):
        row = [int(input("Enter a value: ")) for _ in range(cols)]
        array.append(row)
    return array

rows_input = int(input("Enter the number of rows: "))
cols_input = int(input("Enter the number of columns: "))

my_2d_array = create_2d_array(rows_input, cols_input)
print("The elements in the 2D array are:", my_2d_array)

#
# # List_num=[]
# # new_list=[]
# # for i in range(21):
# #     List_num.append(i)
# #     tuplenum=tuple(List_num)
# #     if i%2==0 in List_num:
# #         new_list.append(i)
# #         new_tuple=tuple(new_list)
# #         print(new_tuple)
#
even_numbers = tuple(i for i in range(2, 21, 2))
print("Tuple of even numbers between 1 and 20:", even_numbers)

#
# name=input("Enter name:")
# age=int(input("Enter age:"))
# grade= input("Enter grade")
#
# student_info={"Name":f"{name}",
#               "age":f"{age}",
#               "Grade":f"{grade}"}
#
# print(student_info)
#
#
# student_info["age"]=int(input("Enter updated age"))
#
# print(student_info)
#
student_info = {
    "Name": input("Enter name: "),
    "Age": int(input("Enter age: ")),
    "Grade": input("Enter grade: ")
}

print("\nStudent Information:")
print(student_info)

# Update age
student_info["Age"] = int(input("Enter updated age: "))
print("\nUpdated Student Information:")
print(student_info)


# import sqlite3
#
# conn=sqlite3.connect("employees.db")
# cursor=conn.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS employees ( EmployeeID PRIMARY KEY INTEGER,EmployeeName TEXT EmployeeSalary REAL)")
# cursor.execute("INSERT INTO employees Values('1',Poowa,200000)")
# cursor.execute("INSERT INTO employees Values('2',KD,20000)")
# cursor.execute("INSERT INTO employees Values('3',Ash,2000)")
# cursor.execute("INSERT INTO employees Values('4',Kani,200000000)")
# cursor.execute("INSERT INTO employees Values('5',Zaks,20000000)")
# cursor.execute("Select EmployeeName,EmployeeNumber From employees where EmployerSalary>50000")
# results=cursor.fetchall()
#
# for row in results:
#     print("Name:",row[1])
#
# conn.commit()
# conn.close()
#

import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS employees (EmployeeID INTEGER PRIMARY KEY , EmployeeName TEXT, EmployeeSalary REAL)")
cursor.execute("INSERT INTO employees VALUES (9, 'Shivek ', 300000)")
cursor.execute("INSERT INTO employees VALUES (10, 'Ummijaan ', 400000000)")
cursor.execute("INSERT INTO employees VALUES (11, 'Babu', 50000000)")
cursor.execute("INSERT INTO employees VALUES (12, 'Khaka', 600000000)")
cursor.execute("INSERT INTO employees VALUES (13, 'Ajie', 770000000)")

cursor.execute("SELECT EmployeeName FROM employees WHERE EmployeeSalary > 50000")
results = cursor.fetchall()

print("\nNames of employees with a salary greater than 50000:")
for row in results:
    print("Name:", row[0])

conn.commit()
conn.close()

# #
# # import tkinter as tk
# #
# # window=tk.Tk()
# #
# # def entername():
# #     name=entry.get()
# #     print(name)
# #     labelName.config(text=f"Hello {name}")
# #
# #
# # window.geometry("300x200")
# # entry=tkinter.Entry(window,width=10)
# # entry.pack()
# # labelName=tk.Label(window,text= " ")
# # entername()
# # button=tk.Button(window,text="Click me",command=entername)
# # button.pack()
# # labelName.pack()
# # window.mainloop()
#
import tkinter as tk

def enter_name():
    name = entry.get()
    label_name.config(text=f"Hello {name}")

window = tk.Tk()
window.geometry("300x200")

entry = tk.Entry(window, width=10)
entry.pack()

label_name = tk.Label(window, text=" ")
label_name.pack()

button = tk.Button(window, text="Click me", command=enter_name)
button.pack()

window.mainloop()


# Day 2

# Lists
#Create a list Of students in our class that is not in alphabetical order
school_names=["Hae_Rang","Anchal","Kazuki"]
#Put the list into alphabetical order
school_names.sort()
print(school_names)
#Using a loop, print the list like the following:
#Anchal is in our class.
#Hae—Rang is in our class.
#Kazuki is in our class.
# for i in school_names:
#     print(i,"is in our class")

for school_name in school_names:
    print(f"{school_name} is in our class")

# Dictionaries


#Create a dictionary called words that maps the following vocabulary words
# hello: buna
#goodbye: la revedere
#thank you:multumesc
#Ask the user to enter an english word (from this list)
#Check to see if the word is in the dictionary. If it is print the result like the
#The word hello is buna in Romanian.
#If the word is not in the dictionary, please print the following:
#Sorry, that word is not in the dictionary.


# words={"hello":"buna",
#        "goodbye":"la revedere",
#        "thank you":"multmesc",}
#
# print(words)
#
# english_word=input("Enter an english word from the list:")
#
# if english_word!=words.keys():
#     print("Please enter an English word")
# else:
#     print("Well done that is an English word")
#
# for keys,values in words:
#     if "buana" in "hello":
#         print("The word hello is buna in Roman")
#
#     else:
#         print("sorry,that word is not in dictionary")

words={"hello":"buna",
       "goodbye":"la revedere",
       "thank you":"multmesc",}

english_word = input("Please enter an Englih word:")

if english_word in words:
    romanian=words[english_word]
    print(f"The word {english_word} is {romanian} in Romanian")
else:
    print("sorry,that word is not in dictionary")





#7 Classes
#Create a class called student
#Give the student the following attributes:
#Name
#Grade
#nationality
#Create a class method to change the grade called changeGrade.

# correct question was Create a class method to change the grade called changeGrade
# Create a student instanance with your name and define the name grade and nationality
# Print the information like the ffg
# Shivaar is in grade userinput
# Shivaar is userinput
# Using the class method changeGrade, change the grade userinput and print "Shivaar is in grade user input"

# class Student:
#     def __init__(self,name,grade,nationality):
#         self.name=name
#         self.grade=grade
#         self.nationality=nationality
#
#     def display_details(self):
#         print("name:",self.name)
#         print("grade:",self.grade)
#         print("nationality:",self.nationality)
#
#     def change_grade(self):
#         self.grade=input("Enter updated grade:")
#         print(self.grade)
#
#
# namee=input("Enter name:")
# Grade=input("Enter grade:")
# Nation=input("Enter nationality:")
#
# Person=Student(namee,Grade,Nation)
#
# print(Person.display_details())
# print(Person.change_grade())


# class Student:
#     def __init__(self,name,grade,nationality):
#         self.name=name
#         self.grade=grade
#         self.nationality=nationality
#
#
#     def change_grade(self,grade):
#         if grade<5 and grade>100:
#             self.grade=grade
#
# namee=input("Enter name:")
# Grade=input("Enter grade:")
# Nation=input("Enter nationality:")
#
# Shivaar=Student(namee,Grade,Nation)
#
# print(Shivaar.change_grade(Grade))
# print()

# Output should display
# Shivaar is in grade user input
# Shivaar nationality is user input
# Shivaar is now in grade user input

class Student:
    def __init__(self, name, grade, nationality):
        self.name = name
        self.grade = grade
        self.nationality = nationality

    def change_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade

name_input = input("Enter name:")
grade_input = int(input("Enter grade:"))
nation_input = input("Enter nationality:")

Shivaar = Student(name_input, grade_input, nation_input)

# Print the initial information
print(f"{Shivaar.name} is in grade {Shivaar.grade}")
print(f"{Shivaar.name} nationality is {Shivaar.nationality}")

# Using the class method change_grade, change the grade
new_grade_input = int(input("Enter new grade:"))
Shivaar.change_grade(new_grade_input)

# Print the updated information
print(f"{Shivaar.name} is now in grade {Shivaar.grade}")


# Tkinter with databases

# Using tkinter with an interface of a button and a couple of entry components
# I want the program to let me enter the data using tkinter components and after I enter the data it puts the information  into a database using sqilte3
# It then reads the database in the console.Is this the right way of doing it?

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
#     c.execute("INSERT INTO address(first_name,last_name,address,city,zipcode) Values(?,?,?,?)",(first_name,last_name,address,zipcode))
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
#
#

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









































