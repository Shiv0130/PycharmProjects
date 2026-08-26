#Write a Python programme to calculate the avg of 10 numbers,get the input from a user and use the while and for loop

sum=0
count=0
while count<10:
    enter_number=int(input(f"Enter number{count+1} :"))
    sum+=enter_number
    count+=1
avg=sum/count
print("The average is:",avg)


for count in range(1,11):
    enter_number=int(input(f"Enter number{count}:"))
    sum += enter_number
avg = sum / count
print("The average is:", avg)


