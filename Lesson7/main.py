
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="\t")
    print()


for i in range(5):
    for j in range(i+1):
        print("*",end="\t")
    print()

#Intially R10 000 is placed in a savings account
# interest is earned at a rate of 7% per year
# and at the end of each year R1000 is placed into the account
# Write a program that calculates the number of years that take for the balance to reach R25 000 using a while loop

iValue = 10000  # initial balance
interest_rate = 0.07  # interest rate of 7%
yearly_deposit = 1000  # yearly deposit of R1000

years = 0  # start with zero years

while iValue < 25000:
    # add interest for the year
    iValue += iValue * interest_rate

    # add yearly deposit
    iValue += yearly_deposit

    # increment years
    years += 1

print("It takes", years, "years for the balance to reach R25,000.")
#Print(“The Change is:%.2f” %,format(change))


