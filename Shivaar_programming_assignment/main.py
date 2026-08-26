# #Q1.1
x=int(input("Enter  number 1:"))
#Requires user input
print("x=",x)#Displays output
y=int(input("Enter Number 2:"))
#Requires user input
print("y=",y)#Displays output
z=x+y
#Stores answer to new variable using addition
print("Addition of z=",z)#Displays output
a=x-y
#Stores answer to new variable using subtraction
print("Subtraction of a=",a)#Displays output
b=x/y
#Stores answer to new variable using division
print("Divison of b=",b)#Displays output
c=x%y
#Stores answer to new variable using modulus(divides and only displays remainder)
print("Modulus of c=",c)#Displays output
x+=1
#Increases the value of x
print("x=",x)#Displays output
y-=1
#Decreases the value of y
print("y=",y)#Displays output

#Q2.2

#Using functions
def is_pangram():
    # Get user input string
    s = input("Enter a string: ")

    # Create a set of lowercase letters in the input string
    letters = set(s.lower())

    # Remove any whitespaces from the set
    letters.discard(' ')

    # Check if the length of the set is equal to 26
    return len(letters) == 26

print(is_pangram())

#Q3.1
quantity=int(input("Enter purchased quantity:"))
#Requires user input

packprice=99
#Assigns the price to variable

if quantity>=10 and quantity<=19:
    discValue=0.1
    #If value quantity is greater then 10 but below 19 then store a discount value of 19%
    print("Discount applied",discValue)
    discAmt=packprice*quantity*discValue
    print("Discount amount", discAmt)
    #Calculates then displays Discount amount
    totalAmt = packprice * quantity - discAmt

elif quantity>=20 and quantity<=49:
    discValue=0.2
    # If value quantity is greater then 20 but below 49 then store a discount value of 10%
    print("Discount applied", discValue)
    discAmt=packprice*quantity*discValue
    print("Discount amount", discAmt)
    # Calculates then displays Discount amount

elif quantity >= 50 and quantity <= 99:
    discValue = 0.3
    # If value quantity is greater then 50 but below 99 then store a discount value of 10%
    print("Discount applied", discValue)
    discAmt = packprice * quantity * discValue
    print("Discount amount", discAmt)
    totalAmt = packprice * quantity - discAmt
    # Calculates then displays Discount amount

if quantity >= 100:
    discValue = 0.4
    # If value quantity is greater then 10 but below 19 then store a discount value of 10%
    print("Discount applied", discValue)
    discAmt = packprice * quantity * discValue
    print("Discount amount", discAmt)
    totalAmt = packprice * quantity - discAmt
    # Calculates then displays Discount amount

else:
    discValue=0
    print("Discount applied", discValue)
    discAmt=0
    print("Discount amount", discAmt)
    totalAmt = packprice * quantity - discAmt


    print("Total Cost:",totalAmt)
    # Calculates then displays Total amount
#

#Q3.2.
rows=int(input("Enter number of rows:")) #Allows for user input
for r in range(rows):#loops r till the number of rows entered above
    for c in range(r+1):#Increases the counter and allows the cloumns to be set
        print("*",end="") #Displays out put of the processes above
    print()#Displays for second loop and formating of the shape


#Q3.3


scores=[0,0,0,0,0]#Stores all the scores
for i in range(5):
    scores[i]=float(input(f" Enter Score{i+1}:"))
#Allows you to write score multiple time in a controlled range of 5


    sum = 0
    for i in range(5):
     sum += scores[i]
#This is to sum up all the scores
    avg = sum / 5
#Declaring your avg which is your sum/total amount of sores
    if avg>=90:
        Avg_Grade= "A"
#Calcultes the criteria of the average
    elif avg >= 80 and avg<= 89:
        Avg_Grade = "B"
    # Calcultes the criteria of the average
    elif avg >= 70 and avg <= 89:
        Avg_Grade = "C"
    # Calcultes the criteria of the average

    elif avg >= 50 and avg <= 69:
        Avg_Grade = "D"
    # Calcultes the criteria of the average

    elif avg >= 0 and avg <= 49:
        Avg_Grade = "F"
#Calcultes the criteria of the average




print("Test scores")
for i in range(5):
    score=scores[i]
#Create a new variable to store all the scores
    if score>=90:
        Grade= "A"
        print("Score: {}, Grade: {}".format(score, Grade))
    # Calcultes the criteria of the score to find out the learners score
    elif score >= 80 and score<= 89:
        Grade = "B"
        print("Score: {}, Grade: {}".format(score, Grade))
        # Calcultes the criteria of the score to find out the learners score
    elif score >= 70 and score <= 89:
        Grade = "C"
        print("Score: {}, Grade: {}".format(score, Grade))
        # Calcultes the criteria of the score to find out the learners score

    elif score >= 50 and score <= 69:
        Grade = "D"
        print("Score: {}, Grade: {}".format(score, Grade))
        # Calcultes the criteria of the score to find out the learners score

    elif score >= 0 and score <= 49:
        Grade = "F"
        print("Score: {}, Grade: {}".format(score, Grade))
        # Calcultes the criteria of the score to find out the learners score

print("Average: {:.2f},Grade {}".format(avg, Avg_Grade))
#Calcultes the criteria of the average to find out the class average















