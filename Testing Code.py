from tabulate import tabulate
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
	try:
		print('''Choose from one of the list of valid input options below:
	1 - If you\'re finished press 1 to exit the program.
	2 - If you want to continue entering other information.
	3 - If you\'d like to view all the information entered in raw format.
	4 - If you\'d like to view the information entered in the form of a table.
			   '''
			 )
		continue_test = int(input('What would you like to do?  '))
	except:
		print('ERROR: Please enter a valid response number. \n')
		continue
	if continue_test == 1:
		break
	elif continue_test == 3:
		print(
			'Names ->',names, '\n'
			'Loan Amounts ->',loan_amounts, '\n'
			'Interest Rates ->',interest_rates, '\n'
			'Loan Durations ->',loan_durations, '\n'
			'Monthly_payments ->',monthly_payments, '\n'
			'Total amount repaid ->',total_loan_repaid, '\n'
			'Compound Interests ->',compound_interests, '\n'
			)
		continue
	elif continue_test == 2:
		loan_amount = 1000.0
		interest_rate = 10.0 / 100
		loan_duration = 10.0
		while isTrue:
			#Getting the name of the user
			name = input('Enter your first name only. ')
			names.append(name)
			#Getting the loan amount
			# ~ loan_amount = float(input("Enter the principal amount: "))
			loan_amounts.append(loan_amount)
			#Getting the interest rate
			# ~ interest_rate = float(input("Enter the interest rate on the loan amount: ")) / 100
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
			

			# ~ #Outputting the results
			print(
f"""For user {name} the total amount to be paid back is ${loan_repaid:,.2f},
the total amount to be paid back monthly is ${monthly_payment:,.2f} and
the compound interest on the loan is ${compound_interest:,.2f} 
			""")
			break
		else:
			print('ERROR: Please enter a valid response number.\n')
	
