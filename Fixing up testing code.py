"""
Calculates total amount to be repaid on a loan, the compound interest and the monthly payment.
Through the use of the amortize_schedule function a table showing all the payments over the years can be generated.
Functions:
	amortize_schedule(value, rate, pmt_yrs)
"""
from beautifultable import BeautifulTable
def amortize_schedule(value, rate, pmt_yrs):
	"""
	This function is used to calculate an amortization schedule and displays 
	a table showing all the payments, the changing loan amount with each payment, 
	the principal, the remaining balance after each payment and the 
	actual amount being paid each time.
	The function accepts three parameters:
	value: This is the loan amount borrowed.
	rate: This is the value of the interest rate that has already been converted to 
	the monthly interest rate.
	pmt_yrs: This represents the number of years given to repay the loan.
	"""
	num_of_months = 0
	intrate = rate
	totalpmts = pmt_yrs * 12
	payment = (value * (intrate * (pow(1 + intrate, totalpmts)))) / (pow((1 + intrate), totalpmts) - 1)
	table = BeautifulTable()
	table.columns.header = ['PAYMENT NO.', 'LOAN VALUE', 'INTEREST', 'PRINCIPAL', 'REMAINING BALANCE', 'PAYMENT']
	
	while value > 0:
		num_of_months += 1
		
		interest = (value * intrate)
		principal = payment - interest
		
		if value - payment < 0:
			principal = value
		table.rows.append([num_of_months, value, interest, principal, value-principal, payment])
		
		value -= principal
		
	print(table)
	
names = []
loan_amounts = []
interest_rates = []
loan_durations = []
monthly_payments = []
total_loan_repaid = []
compound_interests = []
counter = 0
while True:
	# ~ counter += 1
	try:
		print('''Choose from one of the list of valid input options below:
	\t1. If you\'re finished press 1 to exit the program.
	\t2. If you want to continue entering other information.
	\t3. If you\'d like to view all the information entered in raw format.
	\t4. If you\'d like to view the information entered in the form of a table.
	\t5. Choose this option to display the entered info. in table form and end the program.
			   ''')
		option = int(input('What would you like to do?  '))
	except ValueError:
		print('ERROR: Please enter a valid response number. \n')
		continue
	
	if option == 3:
		#This option right here I'm just printing out the plain list
		print(f'''
			 Names -> {names}
			 Loan Amounts -> {loan_amounts},
			 Interest Rates -> {interest_rates},
			 Loan Durations -> {loan_durations},
			 Monthly_payments -> {monthly_payments},
			 Total amount repaid -> {total_loan_repaid},
			 Compound Interests -> {compound_interests}
			''')
		continue
	elif option == 2:
		# ~ loan_amount = 1000.0
		# ~ interest_rate = 10.0 / 100
		# ~ loan_duration = 10.0
		# ~ totalpmts = loan_duration * 12
		while True:
			try:
				#Getting the name of the user
				name = input('Enter your first name only. ')
				names.append(name)
				#Getting the loan amount
				loan_amount = float(input("Enter the principal amount: "))
				loan_amounts.append(loan_amount)
				#Getting the interest rate
				interest_rate = float(input("Enter the interest rate on the loan amount: ")) / 100
				interest_rate = interest_rate / 12
				interest_rates.append(round(interest_rate, 2))
				#Getting the loan duration
				loan_duration = float(input("Enter the number of years that you have to repay the loan: "))
				periods = loan_duration * 12
				loan_durations.append(loan_duration)
				# ~ totalpmts = loan_duration * 12
			except ValueError:
				print('ERROR: Please enter a valid response.')
			
			# ~ loan_amount = 1000.0
			# ~ interest_rate = 10.0 / 100
			# ~ loan_duration = 10.0
		#Calculation Section
	
			#Calculating the monthly payment using the formula
			monthly_payment = (loan_amount * (interest_rate * (pow((1 + interest_rate), periods)))) / ((pow((1 + interest_rate), periods) - 1))
			# ~ monthly_payment = loan_amount *(interest_rate * (1 + interest_rate) ** loan_duration*12) / ((1 + interest_rate) ** loan_duration*12) - 1
			monthly_payments.append(round(monthly_payment, 2))
			# ~ monthly_payment = loan_amount *(interest_rate * (1 + interest_rate) ** loan_duration) / ((1 + interest_rate) ** loan_duration)
			# ~ unpaid_balance = loan_amount * ((1 + interest_rate) ** loan_duration) - (monthly_payment / interest_rate) * (((1 + interest_rate) ** loan_duration) - 1)
			# ~ monthly_payment = loan_amount *(interest_rate * (1 + interest_rate) ** loan_duration*12) / ((1 + interest_rate) ** loan_duration*12) - 1
			# ~ monthly_payments.append(round(monthly_payment, 2))
		
			# ~ #Calculating the total amount to be repaid
			loan_repaid = monthly_payment * loan_duration * 12
			total_loan_repaid.append(round(loan_repaid, 2))
		
			# ~ #Calculating the compound interest
			compound_interest = loan_amount * (1 + ((interest_rate * 12)/ 1)) ** (1 * loan_duration)
			compound_interests.append(round(compound_interest, 2))
			

			# ~ #Outputting the results
			print(
f"""\nFor the loan amount of ${loan_amounts[counter]:,.2f}.
\nThe total amount to be paid back is ${total_loan_repaid[counter]:,.2f},
\nthe total amount to be paid back monthly is ${monthly_payments[counter]:,.2f} and
\nthe compound interest on the loan is ${compound_interests[counter] - loan_amounts[counter]:,.2f}
			""")
			counter += 1
			break
		else:
			print('ERROR: Please enter a valid response number.\n')
	elif option == 1:
		break
	elif option == 4:
		amortize_schedule(loan_amount, interest_rate, loan_duration)
		continue
	elif option == 5:	
		amortize_schedule(loan_amount, interest_rate, loan_duration)
		break
		
	
