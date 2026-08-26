mark=int(input("Enter mark:"))
if mark>=75:
    print("Distinction")

elif mark>=50 and mark<=74:
    print("Credit")

elif mark>=60 and mark<=59:
    print("Pass")

if mark<50:
     print("Fail")

userNum1=int(input("Enter number "))
userNum2=int(input("Enter last number"))
i=userNum1
end=userNum2 
while i<=end:
  print(i)
  i+=1

#find avg of 1 to 5 and the avg


i = 1
end = 5
sum = 0

while i <= end:
    print(i)
    i += 1
    sum +=i

avg = int(sum/i)
print("Average", avg)


#Write a python program that asks several users for the username and password if the username is your name and the password is eqauls to 102030,the prgram should print log in successful if the username and passowrd are both correct else the program should print incorrect details

my_name="Shivaar"
my_password="102030"



login_successful = False

while not login_successful:
 username=input("Enter username:")
 password=input("Enter password:")

 if username==my_name and password==my_password:
  print("login successful")
  login_successful= True

 else:
  print("Incorrect details,try again")



















