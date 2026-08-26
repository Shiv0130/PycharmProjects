# even_numbers=[2,4,6,8,10]
# print(even_numbers)
#
# test = ["Bob",30,8745.13]
# print(test)
#
# numbers = [99,100,101,102]
# for n in numbers:
#     print(n)
#
# # my_list=[5,10,15,20]
# # print(my_list[0], my_list[1], my_list[2], my_list[3])
#
# my_list=[10,20,30,40]
# index = 0
# while index < 4:
#     print(my_list[index])
#     index+=1
#
# nos=[1,2,3,4,5]
# print(nos)
# nos[0]=99
# print(nos)
#
# nos[1]="Bob"
# print(nos)
#
#
# NUM_DAYS = 5
#
#
# def main1():
#     # Create a list to hold the sales for each day.
#     sales = [0] * NUM_DAYS
#
#     # Create a variable to hold an index.
#     index = 0
#
#     print("Enter the sales for each day:")
#
#     # Get the sales for each day.
#     while index < NUM_DAYS:
#         print("Day #", index + 1, ":", sep=" ", end=" ")
#
#         # Input from the user (no try/except block)
#         user_input = input()
#
#         # Convert input to float (no try/except block)
#         sales[index] = float(user_input)
#
#         index += 1
#
#     # Display the values entered.
#     print("Here are the values you entered:")
#
#     for value in sales:
#         print(value)
#
#
# # Call the main function.
# main1()
#
#
# list1=[1,2,3,4]
# list2=[4,5,6,7]
# list3=list1+list2
#
# girl_names=["Joane","Karen","Lori"]
# girl_names+=["Jenny","Kelly"]
# print(girl_names)
#
#
# integers=[1,2,3,4,5,6,7,8,9,10]
# print(integers[1:8:2])

# This program demonstrates the in operator
# used with a list.
# def main1_2():
# # First create an empty list.
# names_list=[]
# # Create a variable to control the loop.
# again="y"
# #Add some names to the list.
# while again=="y":
# #     get a name from the user
# name = input("Enter a name:")
# # Append the name to the list:
# names_list.append(name)
# # Add another one?
# print("Do you want to add another name?")
# again= input("y = yes, anything else = no:")
# print()
# # Display the names that were entered.
# print("Here are the names you entered.")
# for name in names_list:
#     print(name)
# #     call the main function.
# main1_2()

# def main2():
#     # Create a list of product numbers.
#     prod_nums = ["V475", "F987", "Q143", "R688"]
#     # Get the product number to search for:
#     search = input("Enter a product number:")
#
#     # Determine whether the product number exists in the list
#     if search in prod_nums:
#         print(search, "was found in the list")
#     else:
#         print(search, "was not found in the list")
#
# # Call the main function
# main2()

# mylist=[9,1,0,2,8,6,7,4,5,3]
# print("Original order:",mylist)
# mylist.sort()
# print("Sorted out:",mylist)
# mylist.reverse()
# print("Reversed:",mylist)
#
# # This program uses a function to calculate the
# # total of the values in a list.
#
# def main3():
#     # Create a list.
#     numbers =[2,4,6,8,10]
#     # Display the total of the list elements.
#     print("The total is", get_total(numbers))
#
# # The get total function accepts list as an
# # argument returns the total values in
# # the list.
# def get_total(value_list):
# #     create a variable to use an accumalator.
# total=0
#
# # Calculate the total of the list elements.
# for num in value_list:
#     total+=num
# #     return the total
# return total
#
# # Call main function.
# main3()
#
# import random
# ROWS = 3
# COLS = 4
#
# def main4():
#     # Create a two-dimensional list.
#     values=[[0,0,0,0],
#             [0,0,0,0],
#             [0,0,0,0]]
#
#     # Fill the list with random numbers.
#     for r in range(ROWS):
#         for c in range(COLS):
#             values[r][c]=random.randint(1,100)
#
#             # Display the random numbers.
#             print(values)
#
#         # Call the main function
#         main4()


# Define a list of even numbers
even_numbers = [2, 4, 6, 8, 10]
print(even_numbers)

# Define a list with mixed data types
test = ["Bob", 30, 8745.13]
print(test)

# Define a list of numbers and iterate through them
numbers = [99, 100, 101, 102]
for n in numbers:
    print(n)

# Define a list and iterate through it using a while loop
my_list = [10, 20, 30, 40]
index = 0
while index < 4:
    print(my_list[index])
    index += 1

# Create a list of numbers and demonstrate element assignment
nos = [1, 2, 3, 4, 5]
print(nos)
nos[0] = 99
print(nos)
nos[1] = "Bob"
print(nos)

# Define a constant for the number of days
NUM_DAYS = 5

# Create a list to store daily sales and calculate the average
def main1():
    sales = [0] * NUM_DAYS
    index = 0
    print("Enter the sales for each day:")
    while index < NUM_DAYS:
        print("Day #", index + 1, ":", sep=" ", end=" ")
        user_input = input()
        sales[index] = float(user_input)
        index += 1
    print("Here are the values you entered:")
    for value in sales:
        print(value)

# Call the main function
main1()

# Concatenate two lists
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
list3 = list1 + list2

# Add names to a list of girl names
girl_names = ["Joane", "Karen", "Lori"]
girl_names += ["Jenny", "Kelly"]
print(girl_names)

# Access a slice of a list
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integers[1:8:2])

# Define an empty list and add names to it using a loop
def main1_2():
    names_list = []
    again = "y"
    while again == "y":
        name = input("Enter a name:")
        names_list.append(name)
        print("Do you want to add another name?")
        again = input("y = yes, anything else = no:")
    print("Here are the names you entered:")
    for name in names_list:
        print(name)

# Call the main function
main1_2()

# Sort and reverse a list
mylist = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print("Original order:", mylist)
mylist.sort()
print("Sorted out:", mylist)
mylist.reverse()
print("Reversed:", mylist)

# Define a list and calculate its total using a function
def main3():
    numbers = [2, 4, 6, 8, 10]
    print("The total is", get_total(numbers))

# Function to calculate the total of a list
def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total

# Call the main function
main3()

# Create a two-dimensional list with random numbers
import random
ROWS = 3
COLS = 4

def main4():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
            print(values)

# Call the main function
main4()
