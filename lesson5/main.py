# #Recap
#1.x=5 and y=10 print if x is less than 10 and y is greater than 5 ,print condition is true else print condition is false

x=5
y=10
if x<10 and y>5:
    print("Condition is true")
else:
    print("Condition is false")

#2.Check if x is equal to 5 or why is less than 10


x = 5
y = 10
if x==5 or y > 10:
        print("Condition is true")
else:
        print("Condition is false")

#3.given x=5 print the condition if x is not equal to 100


x=5
if x!=100:
    print("The condition is false")

for number in range(3):
    print("Attempt",number)


for number in range(1,4):
    print("Attempt",number+1)

for number in range(1,10,2):
    print("Attempt",number+1)
from itertools import groupby

#check if x =10 from user input and print attempt successful 3 times if not print attempt fail

x=int(input("Enter a number:"))
if x==10:
    for i in range(1,4):
        print("Attempt successful")
else:
        print("Attempt failed")

#Write a program in python that gives the user three chances to enter the correct details
# if the user enters the username and password correctly,
# the program prints access granted and exits the loop,
# if the user enters incorrect credientails too many times
# which is more than 3 times the program prints to many incorrect attempts accessed denied and exits the loop

# pass_name="Shivaar"
# gPass=2301
#
# login_succesful=False
#
# for i in range(3):
#     username = input("Enter name:")
#     password = input("Enter password:")
#
#     if username==pass_name and password==gPass:
#         print("Access granted")
#         login_succesful=True
#         break
#
#     else:
#         print("Incorrect username or password.Please try again")
#
#         if not login_succesful:
#             print("Too many incorrect attempts.Access denied.")

# pass_name = "Shivaar"
# gPass = "2301"
# login_successful = False
#
# for attempt in range(3):
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#
#     if username == pass_name and password == gPass:
#         print("Access granted!")
#         login_successful = True
#         break
#
#     else:
#         print("Incorrect username or password. Please try again.")
#
# if not login_successful:
#     print("Too many incorrect attempts. Access denied.")


name='Shivaar'
passcode="2301"
for attempts in range(3):
    username=input("Enter username:")
    password=input("Enter password:")

    if username==name and password==passcode:
        print('Access granted')

        break

    else:
        print("Incorrect username or password")

else:
    print("Too many attempts access denied")




