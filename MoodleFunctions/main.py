def message():
    print("I am Shivaar")
    print("The IT Genius")

message()

#Void function

def greeting(name):
    print("Good to see you coding again",name)

greeting("Mr Sewnarain")

def multiplyNumbers(a,b):
    product=a*b
    print(f"The product of {a} x {b} = {product}")

def addingNumbers(a,b):
    sum=a+b
    print(f"The sum of {a} + {b} = {sum}")

multiplyNumbers(2,3)
addingNumbers(5,7)

def first_function():
    local_variable=10
    print("The local variable in the first function is:",local_variable)

def second_function():
    local_variable=20
    print("The local variable in the first function is:", local_variable)

first_function()
second_function()
#print("The value outside both these functions are",x)

#This program demonstrates an argument being
#passed to a function
def main():
    value=5
    show_double(value)

#The show_double funtion accepts an argument
#and displays its double value
def show_double(number):
        result = number * 2
        print(result)
#call the main function
main()

#Keyword Arguments
def greet(name,message):
    print("Hello there",name,message)

greet(message=" we meet again",name="Shivaar")

#Default arguments
def greet(name,message="Always at your service"):
    print(message,name)

greet("Mr Sewnarain")

#This program demonstartes what happens when you change the value of a parameter.
def mainValue():
    value=99
    print(f"The value is {value}")
    change_me(value)
    print(f"Back in main the value is {value}.")
def change_me(arg):
    print("I'm changing the value.")
    arg=0
    print(f"Now the value is {arg}")
#Call the main function
mainValue()


x=10
def increase_x():
    global x
    x+=1
    print(x)

increase_x()


#Global constant
PI=3.14
def calc_circumference(radius):
    #Accessing the global constant
    circumference=2*PI*radius
    return circumference
#Global variable
circumference=0
#Using the function to calculate the circumference
circumference=calc_circumference(10)
print(circumference)

#This program uses the return value of a function
def mainAge():
    #Get the user's age.
    first_age=int(input("Enter your age:"))
    #Get the user's best friends age.
    second_age=int(input("Enter your best friend's age:"))
    #Get the sum of both ages
    total=sum(first_age,second_age)
    #Display the total age
    print(f"Together you are {total} years old.")
 #The sum function accepts two numeric arguments and# returns the sum of those arguments.
def sum(num1,num2):
    result=num1+num2
    return result
mainAge()

#Example

def sum_of_squares(x,y):
    sum=(x**2) + (y**2)
    return sum
result=sum_of_squares(3,4)
print("The sum of squares is,",result)

#This program displays five random
# numbers in the range 1 through 100.

#Using libraries
import random
def main1():
    for i in range(5):
        print(random.randint(1,100))
main1()

#math module

import math

x=10
y=20

#Square root functiom
result=math.sqrt(x)

#Power function
result=math.pow(x,y)

#factorial functiom
result=math.factorial(x)


