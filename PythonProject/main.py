# import sys
#
# class Employees:
#     def __init__(self,name,age,salary,dept):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.dept = dept
#     def yr_bonus(self):
#         if self.salary < 60000:
#             return  self.salary*0.15
#             sys.exit()
#         elif self.salary >60000 and self.salary < 80000:
#             return self.salary*0.20
#             sys.exit()
#         else:
#          return 0
#
# namee = input("Please enter Employee name:")
# agee = int(input("Please enter Employee age") )
# salaryy = float(input("Please enter Employee salary") )
# deptt = input("Please enter dept")
# emp1 = Employees(namee,agee,salaryy,deptt)
#
# print("The bonus of employee is : " , emp1.yr_bonus())
#
#
#
# # 1. create a python program that calculates the area of a square,
# # it should use a class called shape and a method called calculate area.
#
# class Shape:
#     def __init__(self,width,length):
#         self.width = width
#         self.length =length
#     def calcArea(self):
#         area=self.length*self.width
#         return area
#
# breadth=int(input("Enter breadth:"))
# lengthh=int(input("Enter length:"))
# ShapeOfYou= Shape(breadth,lengthh)
#
# print("The area of the shape is:" , ShapeOfYou.calcArea())

# Define a base class called Shape
class Shape:
    # Constructor to initialize the side length
    def __init__(self, side):
        self.side = side

    # Method to calculate and return the area of the shape
    def CalArea(self):
        area = self.side ** 2
        return area


# Take user input for the side length
s = int(input("Enter side:"))

# Create an instance of the Shape class with the user-provided side length
ShapeOfYou = Shape(s)

# Calculate and print the area of the shape
print("The area of the shape is:", ShapeOfYou.CalArea())







# 2. create a class called vehicle which is an attribute called weight and a method called calculate toll fee,
# if the weight of the vehicle is greater than equal to 10 000kgs the toll fee to be paid is R50.
# If the weight of the vehicle is between 3000kgs and less than equal to 5000kgs ,the toll fee to be paid is R30.
# If the weight of the vehicle is greater than 2000kgs and less than equal to 3000kgs, the toll fee to be paid is R20.

# import sys
# class Vehicle:
#     def __init__(self, weight):
#         self.weight = weight
#
#     def calcTollFee(self):
#         if self.weight>10000:
#             fee="R50"
#             print(fee)
#             sys.exit()
#         elif self.weight>3000 and self.weight<=5000:
#             fee="R30"
#             print(fee)
#             sys.exit()
#        # elif self.weight>2500 and self.weight<3000:
#             #fee="R20"
#             #return fee
#            # sys.exit()
#

# Inheritance
# class Light_Vehicles(Vehicle):
#     def __init__(self,weight,color):
#         self.color = color
#         super().__init__(weight)
#
#         super().calcTollFee()
#
#
#     def calc_Light(self):
#         if self.weight>2000 and self.weight<3000:
#             fee="R10"
#             return fee
#             sys.exit()
#         elif self.weight>1000 and self.weight<=2000:
#             fee="R5"
#             return fee
#             sys.exit()
#
#
# class Motorcycle(Vehicle,Light_Vehicles):
#     def __init__(self, weight):
#         self.weight = weight
#
#         super().__init__(weight)
#         super().calcTollFee()
#         super().calc_Light()




# weightt=int(input("Enter weight of vehicle:"))
# cars=Light_Vehicles(weightt)
#
# print("The toll fee of the car is:" ,cars.calc_Light())

# Write a Python class called square and define two methods that return the square area and perimeter.
# Define a subclass called Square that inherits from the Shape class
class Square(Shape):
    def __init__(self, side):
        # Call the constructor of the parent class (Shape) and pass the side length
        super().__init__(side)

    # Method to calculate and return the perimeter of the square
    def CalcPerimeter(self):
        perimeter = 4 * self.side
        return perimeter


# Create an instance of the Square class with the same side length as the Shape class
SquareP = Square(s)

# Calculate and print the perimeter of the square
print("The perimeter of the square is:", SquareP.CalcPerimeter())




# Write a Python program to create a bank account class with deposit and withdraw methods.
# There should be a balance of R10 000 in the account.
# If a person deposits it should increase that balance,
# if a person withdraws it should subtract that balance.
# Use an If condition to check whether there is sufficient amount of money to process a withdrawal.
# And then in the end print the net available balance.

# # Define a bank account class
# class BankAccount:
#     def __init__(self):
#         # Initialize the balance with R10,000
#         self.balance = 10000
#
#     def deposit(self, amount):
#         # Deposit money into the account
#         self.balance += amount
#
#     def withdraw(self, amount):
#         # Check if there is sufficient balance to withdraw
#         if amount <= self.balance:
#             # Withdraw money from the account
#             self.balance -= amount
#         else:
#             print("Insufficient balance to withdraw R{0}".format(amount))
#
#     def check_balance(self):
#         # Return the current balance
#         return self.balance
#
#
# # Create an instance of the BankAccount class
# account = BankAccount()
#
# # Deposit R2,000 into the account
# account.deposit(2000)
#
# # Withdraw R1,500 from the account
# account.withdraw(1500)
#
# # Withdraw R10,000 from the account (attempting to overdraft)
# account.withdraw(10000)
#
# # Check the current balance
# balance = account.check_balance()
#
# # Print the net available balance
# print("Net available balance: R{0}".format(balance))


# Define a bank account class
class BankAccount:
    def __init__(self):
        # Initialize the balance with R10,000
        self.balance = 10000

    def deposit(self, amount):
        # Deposit money into the account
        self.balance += amount

    def withdraw(self, amount):
        # Check if there is sufficient balance to withdraw
        if amount <= self.balance:
            # Withdraw money from the account
            self.balance -= amount
        else:
            print("Insufficient balance to withdraw R{0}".format(amount))

    def check_balance(self):
        # Return the current balance
        return self.balance

# Create an instance of the BankAccount class
account = BankAccount()

# Prompt the user to enter a deposit amount
deposit_amount = float(input("Enter the deposit amount: R"))
account.deposit(deposit_amount)

# Withdraw R1,500 from the account
account.withdraw(1500)

# Withdraw R10,000 from the account (attempting to overdraft)
account.withdraw(10000)

# Check the current balance
balance = account.check_balance()

# Print the net available balance
print("Net available balance: R{0}".format(balance))








