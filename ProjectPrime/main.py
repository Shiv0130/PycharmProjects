#Check Number is Prime or Not

# num=int(input("Enter number:"))
# if num%2==0:
#     print("Yes number is prime")
# else:
#     print("Number isn't prime")
#     num+=1


num=int(input("Enter number:"))
count=0

if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count+=1
    if count==2:
        print("Number is Prime")
    else:
        print("Number isn't prime")


