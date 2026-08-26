#Assuming that they are no accidents or delays,the distance that a car travels down the freeway can be calculated as Distance=Speed*Time,
#a car is travelling at 70km/h wite a python program that displays the following
#the distance the car will travel in 6hrs"
#distance traveled in 30 minutes
#Distance travelled in 15hrs
s=float(input("Enter Speed:"))
t=float(input("Enter time in hrs:"))
d=s*t
print("Distance covered",d,"km",end=" ")
print("In",t,"hrs")
#python program that outputs eligible to vote if user is 18 years or older and not eligible if user is under 18
#get age from the user
name=input("Enter name:")
age=int(input("Enter age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
