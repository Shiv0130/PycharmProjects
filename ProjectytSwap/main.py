#Swap two numbers:
# num1=int(input("Enter number1:"))
# num2=int(input("Input number2:"))
# if num1>0:
#     if num2>0:
#         num2=num1
#     print(num1)
#     print(num2)

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

print("Value of num1 before swapping",num1)
print("Value of num2 before swapping",num2)

# temp=num1 #Num1 value
# num1=num2 #Num 2 value
# num2=temp #Num 1 value

#or
num1,num2=num2,num1
print("Value of num1 after swapping",num1)
print("Value of num2 after swapping",num2)