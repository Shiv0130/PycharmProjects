#Print Fibonnaci Numbers
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))

for i in range(2,10):
    sum=num1+num2
    print(sum,end="\t")
    num1=num2
    num2=sum


