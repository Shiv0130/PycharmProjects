#Look at exam page
# days=5
# hour=8
# rate1=float(input("Enter hourly rate:"))
# rate2=float(input("Enter hourly rate:"))
# deductions=0.86 #86% given by the fact that you add the %'s together and subtract 100 from them e.g.100-14=86
# print("Gross employer 1:",end=" ")
# print(days*hour*rate1)
# print("Gross employer 2:",end=" ")
# print(days*hour*rate2)
# print("Net pay employer 1:",end=" ")
# print(days*hour*rate1*deductions)
# print("Net pay employer 2:",end=" ")
# print(days*hour*rate2*deductions)

# Define hourly rates for employees
hourly_rate_employee1 = 17.63
hourly_rate_employee2 = 13.67

# Define hours worked for the week
hours_worked = 8 * 5  # 5 working days a week, 8 hours a day

# Calculate gross pay for each employee
gross_pay_employee1 = hourly_rate_employee1 * hours_worked
gross_pay_employee2 = hourly_rate_employee2 * hours_worked

# Calculate tax, medical aid and UIF deductions for each employee
tax_rate = 0.1
medical_aid_and_uif_rate = 0.02

tax_deduction_employee1 = gross_pay_employee1 * tax_rate
tax_deduction_employee2 = gross_pay_employee2 * tax_rate
medical_aid_and_uif_deduction_employee1 = gross_pay_employee1 * medical_aid_and_uif_rate
medical_aid_and_uif_deduction_employee2 = gross_pay_employee2 * medical_aid_and_uif_rate

# Calculate net pay for each employee
net_pay_employee1 = gross_pay_employee1 - tax_deduction_employee1 - medical_aid_and_uif_deduction_employee1
net_pay_employee2 = gross_pay_employee2 - tax_deduction_employee2 - medical_aid_and_uif_deduction_employee2

# Print out results
print("Employee 1 Gross Pay: R{:.2f}".format(gross_pay_employee1))
print("Employee 1 Net Pay: R{:.2f}".format(net_pay_employee1))
print("Employee 2 Gross Pay: R{:.2f}".format(gross_pay_employee2))
print("Employee 2 Net Pay: R{:.2f}".format(net_pay_employee2))



#Write a python program that will begin by reading the cost of a meal ordered at a takeaway shop from the user.Yor program will compute the VAT
# and the Tip for the meal.The VAT rate is 15%.The tip is 20% of the meal without VAT and the output from the program should include the VAT amount,tip amount and
# the grand total amount including both  the VAT and the Tip.The user will be reqd to make a payment.

# VAT=0.15
# TIP=0.2
# meal=input("Enter Meal:")
# cost=float(input("Enter Cost:"))
# VatMeal=cost*VAT
# TipMeal=cost*TIP
# GrandTotal=VatMeal+TipMeal+cost
# print("Meal ordered:",meal)
# print("Cost of Meal:",cost)
# print("With just VAT :",VatMeal)
# print("Tip without VAT:",TipMeal)
# print("The GrandTotal is:{:.2f}".format(GrandTotal))

# payment=float(input("Please Pay:"))
# if payment==GrandTotal:
#     print("Exact cost")
#
# elif payment>GrandTotal:
#     totalCash=payment-GrandTotal
#     print("Give customer",totalCash,"back")
#
# else:
#     print("Insufficent funds for meal!")

meal=input("Enter Meal:")
# read the cost of the meal from the user
cost = float(input("Enter the cost of the meal: "))

# calculate the VAT amount
vat_rate = 0.15
vat = cost * vat_rate

# calculate the tip amount
tip_rate = 0.2
tip = (cost - vat) * tip_rate

# calculate the grand total amount
grand_total = cost + vat + tip

# display the VAT, tip, and grand total amounts
print(f"VAT amount: {vat:.2f}")
print(f"Tip amount: {tip:.2f}")
print(f"Grand total amount: {grand_total:.2f}")

# ask the user to make a payment
payment = float(input("Enter the payment amount: "))

# check if the payment is sufficient
if payment >= grand_total:
    change = payment - grand_total
    print(f"Thank you! Your change is {change:.2f}")
else:
    print("Sorry, your payment is not sufficient.")

