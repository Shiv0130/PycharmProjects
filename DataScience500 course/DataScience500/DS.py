# #This needs correction
# # #Write  a program that stores  students name and 3 marks and then prints out the student name and then the average of the three marks.
# # Name = "Shivaar"
# # mark1 = 30
# # mark2 = 60
# # mark3 = 90
# #
# # averageMark = (mark1+mark2+mark3)/3
# # print(Name)
# # print("The average mark is:", averageMark)
# #
# # #Check whether the average mark is greater than 50
# # if(averageMark>=50):
# #     print("Yes it is atleast 50 or higher")
# # else:
# #     print("Smaller than 50")
# from itertools import count
#
# # from operator import index
# #
# # #Declare a variable called email, store an email address, it must have a capital letter and an @ as well as a .za
# # email = "Shivaar0103@gmail.com"
# #
# # #Convert email address to lowercases
# # lowercaseEmail = email.lower()
# # print(lowercaseEmail)
# # #extract the username everything before the @ sign
# # emailSlice = slice(email)
# #
# # print(emailSlice)
# # #Extract the domain
# # emailDomain = slice(emailSlice)
# #
# # #Declare another email address and the username must have a full stop
# # newEmail = "reese.sewnarain@gmail.com"
# # #Replace the full stop with a space
# # if(newEmail == "."):
# #    newEmail = " "
# #
#
# # #Declare a list with marks and add 6 marks
# # marks = [60,70,80,90,100,90]
# #
# # #without using the max,avg and sum built in functions calculate the total and the average mark
# # count = 0
# # maximum = 0
# # sum = 0
# # avg = 0
# # minimum = 999
# # while(marks<6):
# #    if(marks<minimum):
# #       minimum = marks[count]
# #
# #   if(marks>maximum):
# #      maximum = marks[count]
# #
# #    if()
# #
# #    count+=1
#
# # for mark in marks:
# #    if(mark>maximum):
# #       maximum = marks[mark]
# #       print("Max numbers are",maximum)
# #
# #    if(mark>sum):
# #       sum += marks[mark]
# #       print("Sum of marks are" ,sum)
# #
# #    if(mark>avg):
# #       avg = sum / 6
# #       print("Avg mark is:" ,avg)
# #
# #       if(minimum<mark):
# #          minimum = marks[mark]
# #          print("Minimum mark is:" ,minimum)
# #
#
#
# # #Amina 72- pass
# # #Thabo 46 - fail
# # #Create a dictionaru containing 3 students and their marks and print it out in the format mentioned above
# #
# # dictionary = ({"Thabo":72},
# #               {"Amina":46},
# #               {"Shivaar" : 100})
# #
# # for keys in dictionary:
# #    print(keys)
# #
# #    for values in dictionary:
# #       print(values)
#
# #Ask the user to enter a number it must continue to ask the user until the user enters 0 or 60
# number = int(input("Enter a number:"))
# count = 0
# while(number!=0 and number!=60):
#    number = int(input("Enter number:"))
#    print(number)
#
# # while(number!=0):
# #    number = int(input("Enter a number"))
# #    print(number)
# #    if(number == 0):
# #       print("Number cannot equal 0")
# #       break
# #
# #    if(number == 60):
# #       print("Number cannot be 60")
# #       break

#Corrected version

# This needs correction
# #Write  a program that stores  students name and 3 marks and then prints out the student name and then the average of the three marks.
# Name = "Shivaar"
# mark1 = 30
# mark2 = 60
# mark3 = 90
#
# averageMark = (mark1+mark2+mark3)/3
# print(Name)
# print("The average mark is:", averageMark)
#
# #Check whether the average mark is greater than 50
# if(averageMark>=50):
#     print("Yes it is atleast 50 or higher")
# else:
#     print("Smaller than 50")

# ================================================================
# CORRECTED ANSWER - Exercise 1 (Name + 3 marks + average)
# ================================================================
# Good news bro - your logic here was actually already correct!
# The only reason it didn't run is because it was commented out.
# I've just uncommented/cleaned it below exactly as you wrote it.

Name = "Shivaar"
mark1 = 30
mark2 = 60
mark3 = 90

averageMark = (mark1 + mark2 + mark3) / 3  # sum of the 3 marks divided by 3
print(Name)
print("The average mark is:", averageMark)

# Check whether the average mark is greater than 50
if averageMark >= 50:
    print("Yes it is atleast 50 or higher")
else:
    print("Smaller than 50")

from itertools import count

# from operator import index
#
# #Declare a variable called email, store an email address, it must have a capital letter and an @ as well as a .za
# email = "Shivaar0103@gmail.com"
#
# #Convert email address to lowercases
# lowercaseEmail = email.lower()
# print(lowercaseEmail)
# #extract the username everything before the @ sign
# emailSlice = slice(email)
#
# print(emailSlice)
# #Extract the domain
# emailDomain = slice(emailSlice)
#
# #Declare another email address and the username must have a full stop
# newEmail = "reese.sewnarain@gmail.com"
# #Replace the full stop with a space
# if(newEmail == "."):
#    newEmail = " "
#

# ================================================================
# CORRECTED ANSWER - Exercise 2 (Email string handling)
# ================================================================
# Bro, the idea was right but a few things were broken:
# 1) The task says the email needs a capital letter and ".za" in it -
#    "Shivaar0103@gmail.com" has neither, so I changed it to satisfy
#    the requirement (capital "S" + a .za domain).
# 2) slice(email) is WRONG - slice() just builds a "slice object",
#    it does not cut the string for you. To actually grab part of a
#    string you either use string slicing email[start:stop] or
#    the .split() method. I used .split("@") below since it's the
#    cleanest way to separate username from domain.
# 3) if(newEmail == "."): this compares the WHOLE string to a single
#    dot, which will basically never be True. To replace a character
#    INSIDE the string you need .replace(old, new).

email = "Shivaar0103@gmail.co.za"  # has a capital letter, an @, and .za

# Convert email address to lowercase
lowercaseEmail = email.lower()
print(lowercaseEmail)

# Extract the username - everything before the @ sign
emailUsername = email.split("@")[0]  # split() gives ["Shivaar0103", "gmail.co.za"]
print(emailUsername)

# Extract the domain - everything after the @ sign
emailDomain = email.split("@")[1]
print(emailDomain)

# Declare another email address where the username has a full stop
newEmail = "reese.sewnarain@gmail.com"

# Replace the full stop with a space (only replaces the character, not the whole string)
newEmail = newEmail.replace(".", " ")
print(newEmail)

# #Declare a list with marks and add 6 marks
# marks = [60,70,80,90,100,90]
#
# #without using the max,avg and sum built in functions calculate the total and the average mark
# count = 0
# maximum = 0
# sum = 0
# avg = 0
# minimum = 999
# while(marks<6):
#    if(marks<minimum):
#       minimum = marks[count]
#
#   if(marks>maximum):
#      maximum = marks[count]
#
#    if()
#
#    count+=1

# for mark in marks:
#    if(mark>maximum):
#       maximum = marks[mark]
#       print("Max numbers are",maximum)
#
#    if(mark>sum):
#       sum += marks[mark]
#       print("Sum of marks are" ,sum)
#
#    if(mark>avg):
#       avg = sum / 6
#       print("Avg mark is:" ,avg)
#
#       if(minimum<mark):
#          minimum = marks[mark]
#          print("Minimum mark is:" ,minimum)
#

# ================================================================
# CORRECTED ANSWER - Exercise 3 (min/max/total/avg without built-ins)
# ================================================================
# Bro there were a few core bugs in both attempts:
# WHILE VERSION:
#   - "while(marks<6)" compares a LIST to a number - that's invalid,
#     you need to compare the COUNTER to the length of the list,
#     e.g. while(count < len(marks)).
#   - The total (sum) was never actually being added up anywhere.
#   - "if()" was empty - Python needs a condition inside the brackets.
# FOR VERSION:
#   - "for mark in marks" means "mark" is already the VALUE (e.g. 60),
#     not the position. So marks[mark] tries to use the mark itself
#     as an index, which is wrong and will crash for values >= 6.
#   - "if(mark>sum)" doesn't make sense for building a running total -
#     you just add every mark to sum unconditionally.
#   - avg was only being calculated conditionally, and minimum's
#     condition was backwards (minimum<mark instead of mark<minimum).

marks = [60, 70, 80, 90, 100, 90]  # list with 6 marks

count = 0
total = 0  # renamed from "sum" - sum is a Python built-in, best not to overwrite it
maximum = marks[0]
minimum = marks[0]

while count < len(marks):
    total += marks[count]  # add every mark to the running total

    if marks[count] > maximum:
        maximum = marks[count]

    if marks[count] < minimum:
        minimum = marks[count]

    count += 1

avg = total / len(marks)

print("Total of marks is:", total)
print("Average mark is:", avg)
print("Max mark is:", maximum)
print("Min mark is:", minimum)

# #Amina 72- pass
# #Thabo 46 - fail
# #Create a dictionaru containing 3 students and their marks and print it out in the format mentioned above
#
# dictionary = ({"Thabo":72},
#               {"Amina":46},
#               {"Shivaar" : 100})
#
# for keys in dictionary:
#    print(keys)
#
#    for values in dictionary:
#       print(values)

# ================================================================
# CORRECTED ANSWER - Exercise 4 (Student dictionary, pass/fail)
# ================================================================
# Bro a few issues here:
# 1) That's not really a dictionary - {"Thabo":72} inside a tuple/list
#    means you actually made a LIST OF 3 SEPARATE DICTIONARIES.
#    A proper single dictionary looks like:
#    {"Thabo": 72, "Amina": 46, "Shivaar": 100}
# 2) The nested for loop was looping over "dictionary" twice and
#    printing the same dict objects repeatedly instead of looping
#    through name/mark PAIRS.
# 3) There was no pass/fail logic at all, even though the comments
#    at the top show that's exactly the required output format
#    (Amina 72 - pass, Thabo 46 - fail).

students = {"Thabo": 72, "Amina": 46, "Shivaar": 100}  # one dictionary, name -> mark

for name, mark in students.items():  # .items() gives you both the name AND the mark
    if mark >= 50:
        result = "pass"
    else:
        result = "fail"
    print(name, mark, "-", result)

# Ask the user to enter a number it must continue to ask the user until the user enters 0 or 60
number = int(input("Enter a number:"))
count = 0
while (number != 0 and number != 60):
    number = int(input("Enter number:"))
    print(number)

# ================================================================
# NOTE on the block above - Exercise 5 (loop until 0 or 60)
# ================================================================
# Bro this one is actually correct as you wrote it! The while loop
# condition (number != 0 and number != 60) correctly keeps asking
# until either 0 or 60 is entered, then stops. Nice work - I left
# it exactly as-is and active (not commented) since it works.

# while(number!=0):
#    number = int(input("Enter a number"))
#    print(number)
#    if(number == 0):
#       print("Number cannot equal 0")
#       break
#
#    if(number == 60):
#       print("Number cannot be 60")
#       break
#

# ================================================================
# CORRECTED ANSWER - Exercise 5 alternative (break version)
# ================================================================
# Bro this second attempt is a slightly different (also valid) way
# to solve the same problem using break instead of a compound
# condition. The only real bug: your print messages say "cannot
# equal 0" / "cannot be 60" as if those are invalid inputs - but the
# original task just wants the loop to STOP when 0 or 60 is entered,
# not treat them as errors. I fixed the messaging below so it
# reflects what's actually happening.

# number2 = int(input("Enter a number: "))
# while number2 != 0:
#     print(number2)
#     if number2 == 0:
#         print("You entered 0 - stopping.")
#         break
#     if number2 == 60:
#         print("You entered 60 - stopping.")
#         break
#     number2 = int(input("Enter a number: "))

