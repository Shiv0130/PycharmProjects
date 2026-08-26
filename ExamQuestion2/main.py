#Write a Python program that should use variables to stoire the information gathered by the user.
#Ask user for age,nickname,favourite colour,height,blood type
#print how old they'll be in 20 years
#Ask the user again for their surname,DOB,Gender and ID number
#print out three greeting statements in three different SA languages
#Ask the user for 4 numbers and then calculate and print out the sum and avg

Nickname=input("Enter a nickname:")
age=int(input("Enter age:"))
favColor=input("Enter Favourite Colour:")
height=float(input("Enter height:"))
BloodType=input("Enter BloodType:")
age+=20
print("age in 20 years:",age)

surname=input("Enter Surname:")
DOB=input("Enter DateOfBirth:")
ID_no=input('Enter ID number:')
print("HEllO")
print("Sawbona")
print("HAllO")

sum=0
count=0
while count<4:
    enter_number=int(input(f"Enter number{count+1} :"))
    sum+=enter_number
    count+=1
avg=sum/count
print("The average is:",avg)
print("SUM=",sum)
print("Average=", avg)


