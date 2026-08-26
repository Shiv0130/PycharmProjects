#Input a number and check if it's factorial:

factorial=1
num=int(input("Enter number:"))
if num<0:
    print("Factorial doesn't exist for negative numbers")
elif num==0:
    print("The facatorial of 0 is 1")

else:
    for i in range(1,num+1):
        factorial*=i
    print("The factorial of", num ,"is", factorial)