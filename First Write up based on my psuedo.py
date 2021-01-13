#Getting the loan amount
# ~ loan_amount = float(input("Enter the principal amount: "))
# ~ #Getting the interest rate
# ~ interest_rate = float(input("Enter the interest rate on the loan amount: "))
# ~ #Getting the loan duration
# ~ loan_duration = float(input("Enter the number of years that you have to repay the loan: "))
loan_amount = 1000.0
interest_rate = 10.0 / 100
loan_duration = 10.0
#Calculation Section

#Calculating the monthly payment using the formula
monthly_payment = (loan_amount * interest_rate * (1 + interest_rate) ** loan_duration) / ((1 + interest_rate) ** loan_duration - 1)

# ~ #Calculating the total amount to be repaid
loan_repaid = monthly_payment * loan_duration

# ~ #Calculating the compound interest
compound_interest = loan_amount * (1 + (interest_rate / 1)) ** (1 * loan_duration)

# ~ #Outputting the results
print(
f"""The total amount to be paid back is ${loan_repaid:,.2f} 
The total amount to be paid back monthly is ${monthly_payment:,.2f} 
The compound interest on the loan is ${compound_interest:,.2f} 
""")
