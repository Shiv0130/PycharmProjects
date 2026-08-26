# # a. Write a program to add two numbers and display the result.
#
num1=2
num2=3
sum=num1+num2
print("The sum of the two numbers:",sum)
#
# # b. Write a program to calculate the area of a rectangle given its length and width.
length=float(input("Enter Length:"))
width=float(input("Enter Width:"))
area_of_rectangle=length*width
print(area_of_rectangle)
# c. Write a program that converts Celsius to Fahrenheit.
celsius=float(input("Enter Celsius"))
print("Tempreture in Celsius",celsius)
farenheit=(celsius*9.5)+32
print("Tempreture in farenheit ",farenheit)
# # d. Write a program that swaps the values of two variables.
x=1
y=2
print("x then:",x,"y then:",y)
temp=x
x=y
y=temp
print("x now=",x,"y now:",y)
# e. Write a program that calculates the factorial of a number.
#
#
# # Decision Making (if statements):
# # a. Write a program to check if a number is positive, negative, or zero.
number=int(input("Enter number"))
if number>0:
    print("Number is +ve")
elif number<0:
    print("Number is -ve")
elif number==0:
    print("Number is 0")
# b. Write a program that determines if a year is a leap year.

# # c. Write a program to find the largest of three numbers.
# n1=12
# n2=23
# n3=16
# max=0
# if n1>max:
#     max=n1
# elif n2>max:
#     max=n2
#
# if n3>max:
#     max=n3
#     print("The maximum number is:",max)

n1 = int(input("Enter number"))
n2 = int(input("Enter number"))
n3 = int(input("Enter number"))

max = n1  # Assign one of the numbers as the initial maximum

if n2 > max:
    max = n2

if n3 > max:
    max = n3

print("The maximum number is:", max)


# d. Write a program that checks if a number is prime.
num=int(input("Enter number:"))
for i in range(1,num+1):
    if (num%i==0):
        print("The number is prime")
    else:
        print("Number is composite")

# e. Write a program that determines if a character is a vowel or a consonant.
#
# Iteration (while loops):
# a. Write a program to print numbers from 1 to 10 using a while loop.
num=0
while num<10:
    print(num+1)
    num+=1

# b. Write a program to calculate the sum of all numbers from 1 to 100 using a while loop.
count=0
sum=0
while count<100:
    print(count)
    sum += count
    count+=1
print("The sum is:",sum)

# c. Write a program to find the factorial of a number using a while loop.
num = int(input("Enter a number: "))  # Input the number

factorial = 1  # Initialize the factorial to 1

# Calculate factorial using a while loop
while num > 0:
    factorial *= num
    num -= 1



print("The factorial of the number is:", factorial)





# d. Write a program that counts the number of digits in a given number using a while loop.
# e. Write a program to reverse a given number using a while loop.
#
# Iteration (for loops):
# a. Write a program to print even numbers from 1 to 20 using a for loop.
for i in range(21):
    print(i)
# b. Write a program to calculate the sum of all numbers from 1 to 100 using a for loop.
for i in range(101):
    sum+=i
print(sum)
# c. Write a program to find the factorial of a number using a for loop.

# d. Write a program that prints the multiplication table of a given number using a for loop.
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end="\t")
print()

# e. Write a program to find the sum of digits in a given number using a for loop.



num=10
sum=0
for i in range(1,num+1):

    sum+=num
print(f"The sum of the {num} numbers are:",sum)



# a. Write a program to add two numbers and display the result.
num1 = 2
num2 = 3
sum = num1 + num2
print("The sum of the two numbers:", sum)

# b. Write a program to calculate the area of a rectangle given its length and width.
length = float(input("Enter Length:"))
width = float(input("Enter Width:"))
area_of_rectangle = length * width
print("Area of the rectangle:", area_of_rectangle)

# c. Write a program that converts Celsius to Fahrenheit.
celsius = float(input("Enter Celsius: "))
print("Temperature in Celsius:", celsius)
fahrenheit = (celsius * 9/5) + 32  # Correction: Use 9/5 instead of 9.5
print("Temperature in Fahrenheit:", fahrenheit)

# d. Write a program that swaps the values of two variables.
x = 1
y = 2
print("x then:", x, "y then:", y)
x, y = y, x  # Correction: Swap the values using multiple assignment
print("x now =", x, "y now:", y)

# e. Write a program that calculates the factorial of a number.
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("The factorial of the number is:", factorial)

# Decision Making (if statements):
# a. Write a program to check if a number is positive, negative, or zero.
number = int(input("Enter number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# b. Write a program that determines if a year is a leap year.
year = int(input("Enter year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# c. Write a program to find the largest of three numbers.
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

max_num = n1

if n2 > max_num:
    max_num = n2

if n3 > max_num:
    max_num = n3

print("The maximum number is:", max_num)

# d. Write a program that checks if a number is prime.
number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# e. Write a program that determines if a character is a vowel or a consonant.
character = input("Enter a character: ")
vowels = ['a', 'e', 'i', 'o', 'u']

if character.lower() in vowels:
    print(character, "is a vowel")
else:
    print(character, "is a consonant")

# Iteration (while loops):
# a. Write a program to print numbers from 1 to 10 using a while loop.
num = 1
while num <= 10:
    print(num)
    num += 1

# b. Write a program to calculate the sum of all numbers from 1 to 100 using a while loop.
count = 1
sum = 0

while count <= 100:
    sum += count
    count += 1

print("The sum is:", sum)

# c. Write a program to find the factorial of a number using a while loop.
num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("The factorial of the number is:", factorial)

# d. Write a program that counts the number of digits in a given number using a while loop.
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)

# e. Write a program to reverse a given number using a while loop.
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10

print("Reversed number:", reversed_num)

# Iteration (for loops):
# a. Write a program to print even numbers from 1 to 20 using a for loop.
for i in range(2, 21, 2):
    print(i)

# b. Write a program to calculate the sum of all numbers from 1 to 100 using a for loop.
sum = 0

for i in range(1, 101):
    sum += i

print("The sum is:", sum)

# c. Write a program to find the factorial of a number using a for loop.
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("The factorial of the number is:", factorial)

# d. Write a program that prints the multiplication table of a given number using a for loop.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# e. Write a program to find the sum of digits in a given number using a for loop.
num = int(input("Enter a number: "))
sum = 0

for digit in str(num):
    sum += int(digit)

print("Sum of digits:", sum)


