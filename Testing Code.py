#Lists for storing the information entered by the user
names = []
loan_amounts = []
interest_rates = []
loan_durations = []
monthly_payments = []
total_loan_repaid = []
compound_interests = []
isTrue = True
while isTrue:
	continue_test = int(input('Enter 1 if you\'re finish or 2 if you want to continue or if you\'d like to view all that was entered enter the number 3. '))
	if continue_test == 1:
		break
	elif continue_test == 3:
		print('\n')
		print('Names ->',names,
			'Loan Amounts ->',loan_amounts,
			'Interest Rates ->',interest_rates,
			'Loan Durations ->',loan_durations,
			'Monthly_payments ->',monthly_payments,
			'Total amount repaid ->',total_loan_repaid,
			'Compound Interests ->',compound_interests
			)
	#Getting the name of the user
	name = input('What is your name? ')
	names.append(name)
	#Getting the loan amount
	loan_amount = float(input("Enter the principal amount: "))
	loan_amounts.append(loan_amount)
	#Getting the interest rate
	interest_rate = float(input("Enter the interest rate on the loan amount: "))
	interest_rate = interest_rate / 100
	interest_rates.append(interest_rate)
	#Getting the loan duration
	loan_duration = float(input("Enter the number of years that you have to repay the loan: "))
	loan_durations.append(loan_duration)
	# ~ loan_amount = 1000.0
	# ~ interest_rate = 10.0 / 100
	# ~ loan_duration = 10.0
	#Calculation Section

	#Calculating the monthly payment using the formula
	monthly_payment = (loan_amount * interest_rate * (1 + interest_rate) ** loan_duration) / ((1 + interest_rate) ** loan_duration - 1)
	monthly_payments.append(monthly_payment)

	# ~ #Calculating the total amount to be repaid
	loan_repaid = monthly_payment * loan_duration
	total_loan_repaid.append(loan_repaid)

	# ~ #Calculating the compound interest
	compound_interest = loan_amount * (1 + (interest_rate / 1)) ** (1 + loan_duration)
	compound_interests.append(compound_interest)

	# ~ #Outputting the results
	print(
	f"""For user {name} the total amount to be paid back is ${loan_repaid:,.2f},
	the total amount to be paid back monthly is ${monthly_payment:,.2f} and
	the compound interest on the loan is ${compound_interest:,.2f} 
	""")
	continue
