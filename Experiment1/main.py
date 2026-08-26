
#Check if number is a prime no.

num=int(input("Enter number:"))
count=0

if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count+=1


    if count==2:
        print("Number is prime")
    else:
                print("Number isn't prime")




#Check if string is palindrome:

s=input("Enter a string:")

revstr=(s[::-1])

if revstr==s:
    print("Palindrome")
else:
    print("Not Palindrome")