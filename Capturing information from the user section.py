names = []
loan_amounts = []
interest_rates = []
loan_durations = []
monthly_payments = []
total_loan_repaid = []
compound_interests = []

#Getting the name of the user
name = input('What is your name? ')
names.append(name)
#Getting the loan amount
# ~ loan_amount = float(input("Enter the principal amount: "))
loan_amounts.append(loan_amount)
#Getting the interest rate
# ~ interest_rate = float(input("Enter the interest rate on the loan amount: "))
# ~ interest_rate = interest_rate / 100
interest_rates.append(interest_rate)
#Getting the loan duration
# ~ loan_duration = float(input("Enter the number of years that you have to repay the loan: "))
loan_durations.append(loan_duration)
# ~ loan_amount = 1000.0
# ~ interest_rate = 10.0 / 100
# ~ loan_duration = 10.0
#Calculation Section

#Calculating the monthly payment using the formula
monthly_payment = (loan_amount * interest_rate * (1 + interest_rate) ** loan_duration) / ((1 + interest_rate) ** loan_duration - 1)
monthly_payments.append(round(monthly_payment, 5))

# ~ #Calculating the total amount to be repaid
loan_repaid = monthly_payment * loan_duration
total_loan_repaid.append(round(loan_repaid, 5))

# ~ #Calculating the compound interest
compound_interest = loan_amount * (1 + (interest_rate / 1)) ** (1 + loan_duration)
compound_interests.append(round(compound_interest, 5))
