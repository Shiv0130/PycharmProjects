# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# namee=input("Enter name:")
# agee=int(input("Enter age:"))
#
# Persons=Person(namee,agee)
# print(Persons.name, Persons.age)
#
# class Student(Person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#     def OtherDetails(self,grade,school):
#         self.grade=grade
#         self.school=school
#         print("Grade:",grade)
#         print("School:",school)
#
# gradee=int(input("Enter your grade:"))
# schhool=input("Enter your school:")
#
# print(Persons.name , Persons.age , Student.OtherDetails(gradee,schhool))
#
# import tkinter as tk
#
# window=tk.Tk()
# button = tk.Button(window,text="Click me")
#
#
# import sqlite3
#
# conn=sqlite3.connect("students.db")
# cursor= conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS students(StudentName TEXT,Grade Integer,Age INTEGER, FEES REAL)")
# cursor.execute("INSERT INTO students VALUES('Shivaar',13,20,2000.99)")
# cursor.execute("INSERT INTO students VALUES('Shivek',16,23,2003.99)")
# cursor.execute("INSERT INTO students VALUES('Khanna',100,49,1975.99)")
# cursor.execute("INSERT INTO students VALUES('Khaka',101,52,1969.99)")
# conn.commit()
# conn.close()

#Correction
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, grade, school):
        super().__init__(name, age)
        self.grade = grade
        self.school = school

    def print_details(self):
        super().print_details()
        print("Grade:", self.grade)
        print("School:", self.school)

import tkinter as tk


def greet():
    name=name_entry.get()
    greeting_label.config(text= f"Hello {name}")

window=tk.Tk()
window.title("Greeting app")
window.geometry("300x200")

name_label=tk.Label(window,text="Enter your name:")
name_label.pack()

name_entry=tk.Entry(window)
name_entry.pack()

greeting_label=tk.Label(window,text="")
greeting_label.pack()

greeting_button=tk.Button(window,text="Click me for greeting",command=greet)
greeting_button.pack()

window.mainloop()

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(StudentName TEXT,Grade Integer,Age INTEGER, FEES REAL)")
# Add a new student record
cursor.execute("INSERT INTO students (StudentName, Grade, Age, FEES) VALUES (?, ?, ?, ?)",
               ("John", 10, 15, 1500.99))

# Update an existing student's grade
cursor.execute("UPDATE students SET Grade = ? WHERE StudentName = ?",
               (11, "John"))

# Retrieve the names of all students in the database
cursor.execute("SELECT StudentName FROM students")
students = cursor.fetchall()
for student in students:
    print(student[0])

conn.commit()
conn.close()

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"


