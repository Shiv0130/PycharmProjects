# #Practical questions
#
#1
print("Hello World!")

#2
length=float(input("Enter length:"))
breadth=float(input("Enter breadth"))
area=length*breadth
print(f"The area of the rectangle is:{area:.2f}")

#Topic 3

#1
age=int(input("Enter age:"))
if age<18:
    print("You're a minor")
else:
    print("You are an adult")


#2
password="Khaka"
enter_to_access=input("Enter the password:")

if enter_to_access==password:
    print("Access granted")
else:
    print("Access denied")

#Topic 4

#1
num=int(input("Enter number:"))
sum=0
count=0
while num<=1:
    num=int(input(f"Enter number{count+1}:"))
    sum+=num
print(f"The sum of all the numbers are:{sum:.2f}")
count+=1

#2
num=int(input("Enter number:"))
sum=0
count=0
while num!=-1:
    num=int(input(f"Enter number{count+1}:"))
    sum+=num
print(f"The sum of all the numbers are:{sum:.2f}")
count+=1

#Topic 5

#1
def calculate_area(length,breadth):
    area=length*breadth
    print(area)

calculate_area(5,8)

#2

#Topic 6

#1

file=open("input.txt","r")
contents=file.read()
print(contents)
file.close()

#2
file=open("output.txt","w")
file.write("Something" "\n")
file=open("output.txt","w")
file.read()
file.close()

