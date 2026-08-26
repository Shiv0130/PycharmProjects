# Basic Fundamentals:
# a. Write a program that calculates the total cost of a shopping cart with multiple items, including taxes and discounts
# Assuming each item in the cart has a price and quantity
# Tax rate is 10%
# Discount is 20% if the total cost is above 100

cart = [
    {"item": "Item 1", "price": 10, "quantity": 2},
    {"item": "Item 2", "price": 15, "quantity": 1},
    {"item": "Item 3", "price": 5, "quantity": 4}
]

total_cost = 0
for item in cart:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total

tax = total_cost * 0.1

if total_cost > 100:
    discount = total_cost * 0.2
else:
    discount = 0

final_cost = total_cost + tax - discount

print("Total cost:", final_cost)

# b. Write a program that converts a given amount of money in one currency to another currency, using the current exchange rate.
# Assuming exchange rate is 1 USD = 0.85 EUR

usd_amount = 100

exchange_rate = 0.85
eur_amount = usd_amount * exchange_rate

print("USD:", usd_amount)
print("EUR:", eur_amount)

# c. Write a program that generates a random password for a user, considering length and complexity requirements.
# d. Write a program that calculates the BMI (Body Mass Index) of a person based on their height and weight.
height = 1.75  # in meters
weight = 70  # in kilograms

bmi = weight / (height ** 2)

print("BMI:", bmi)

# Decision Making (if statements):
# a. Write a program that determines whether a given year is a leap year or not, taking into account exceptions for centuries.
year = 2024

is_leap_year = False

if year % 4 == 0:
    if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
        is_leap_year = True

if is_leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# b. Write a program that validates a user's password based on certain criteria (e.g., minimum length, presence of uppercase, lowercase, and special characters).
# password = "Password123"
#
# is_valid = True
#
# if len(password) < 8:
#     is_valid = False
# elif not any(char.isupper() for char in password):
#     is_valid = False
# elif not any(char.islower() for char in password):
#     is_valid = False
# elif not any(char.isdigit() for char in password):
#     is_valid = False
# elif not any(char in string.punctuation for char in password):
#     is_valid = False
#
# if is_valid:
#     print("Password is valid")
# else:
#     print("Password is not valid")

# c. Write a program that categorizes a given age into "child," "teenager," "adult," or "senior citizen." #0-12 ,13-19,20-59 60 onwards
age=int(input("Enter age:"))
if age>=0 and age<=12:
    print("You're a lytie")
elif age>=13  and age<=19:
    print("Welcome to teenagehood")
elif age>=20  and age<=59:
    print("Welcome to Adulthood")
else:
    print("Hello senior citizen:)")

# d. Write a program that determines if a given number is a prime number or a composite number.
    num = int(input("Enter number:"))
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if (num % i) == 0:
                count += 1
        if count == 2:
            print("Number is Prime")
        else:
            print("Number composite")

# e. Write a program that checks if a given string is a palindrome (reads the same forwards and backward).
string = input("Enter string:")
is_palindrome = True

for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")

#
# Iteration (while loops):
# a. Write a program that simulates a simple guessing game, where the user has to guess a randomly generated number.
# b. Write a program that prompts the user for a series of numbers until they enter a negative number, then calculates the average of the entered numbers.
# count=0
# sum=0
# num=int(input("Enter number1:"))
# while num!=0:
#     num=int(input(f"Enter number{count+2}:"))
#     sum+=num
#     count+=1
#     avg=sum/count
# print("The sum of all the numbers are:",sum)
# print("The average is:",avg)

count = 0
sum = 0
num = int(input("Enter number:"))

while num >= 0:
    sum += num
    count += 1
    num = int(input(f"Enter number {count+1}:"))

# Handle the case where no numbers were entered
if count == 0:
    avg = 0
else:
    avg = sum / count

print("The sum of all the numbers is:",sum)
print("The average is:", avg)

# c. Write a program that generates the Fibonacci sequence up to a given number using a while loop.
num = int(input("Enter a number: "))  # Input the number

n1, n2 = 0, 1
print(n1, end="\t")  # Print the first Fibonacci number
print(n2, end="\t")  # Print the second Fibonacci number

while n2 <= num:
    nth = n1 + n2
    if nth > num:
        break
    print(nth, end="\t")
    n1 = n2
    n2 = nth

# d. Write a program that prompts the user for a password until they enter the correct password, with a maximum number of attempts.
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

# e. Write a program that counts the number of vowels in a given string using a while loop.
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"  # List of vowels
count = 0

for char in input_string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Iteration (for loops):
# a. Write a program that prints the multiplication table of numbers 1 to 10.
for i in range(1, 11):
    print("Multiplication table for", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

# b. Write a program that calculates the sum of all prime numbers between 1 and 100.
sum_primes = 0

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print("Sum of prime numbers between 1 and 100:", sum_primes)

# c. Write a program that iterates over a list of names and prints a personalized greeting for each name.
names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print("Hello,", name, "! How are you today?")

# d. Write a program that finds and displays all the factors of a given number using a for loop.
number = int(input("Enter a number: "))

print("Factors of", number, "are:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# e. Write a program that prints the first 10 terms of the geometric progression starting from a given number and wth a common ratio.
start = int(input("Enter the starting number: "))
ratio = int(input("Enter the common ratio: "))

print("First 10 terms of the geometric progression:")

for i in range(10):
    term = start * (ratio ** i)
    print(term)
