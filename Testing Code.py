from prettytable import PrettyTable
#Lists for storing the information entered by the user
names = []
loan_amounts = []
interest_rates = []
loan_durations = []
monthly_payments = []
total_loan_repaid = []
compound_interests = []
isTrue = True
columns = ['Names', 'Loan Amount', 'Interest Rate', 'Loan Duration', 'Monthly Payment', 'Total Loan Repaid', 'Compound Interest']
tab = PrettyTable()
while isTrue:
	try:
		print('''Choose from one of the list of valid input options below:
	1 - If you\'re finished press 1 to exit the program.
	2 - If you want to continue entering other information.
	3 - If you\'d like to view all the information entered in raw format.
	4 - If you\'d like to view the information entered in the form of a table.
	5 - Choose this option to display the entered info. in table form and end the program.
			   '''
			 )
		continue_test = int(input('What would you like to do?  '))
	except:
		print('ERROR: Please enter a valid response number. \n')
		continue
	if continue_test == 1:
		break
	elif continue_test == 3:
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
	elif continue_test == 4:
		#I'm using a module called the Prettytable module to create the table, what I'm doing is creating a column(from top to bottom)
		#All the lines down below follow this format ->
		#The first argument before the comma is the name of the column and the second argument after the comma is what is place below that specific column
		#So for the first one 'columns[0] from the columns list represents the string 'Name' so thats the column name and then the list comprehension that I have as the second argument is all the names in the names list
		tab.add_column(columns[0], [name for name in names])
		tab.add_column(columns[1], [loan for loan in loan_amounts])
		tab.add_column(columns[2], [(100 * intRate) for intRate in interest_rates])
		tab.add_column(columns[3], [year for year in loan_durations])
		tab.add_column(columns[4], [monthly for monthly in monthly_payments])
		tab.add_column(columns[5], [total for total in total_loan_repaid])
		tab.add_column(columns[6], [compound for compound in compound_interests])
		#Printing the table
		print(tab)
		#Deleting all the information from the table, because if I don't do this it starts looking ugly really fast
		tab.clear()
		continue
	elif continue_test == 5:
		#This option doesn't have to be here but this was just to have an option to print the table and then end the program
		tab.add_column(columns[0], [name for name in names])
		tab.add_column(columns[1], [loan for loan in loan_amounts])
		tab.add_column(columns[2], [(100 * intRate) for intRate in interest_rates])
		tab.add_column(columns[3], [year for year in loan_durations])
		tab.add_column(columns[4], [monthly for monthly in monthly_payments])
		tab.add_column(columns[5], [total for total in total_loan_repaid])
		tab.add_column(columns[6], [compound for compound in compound_interests])
		print(tab)
		break
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
			monthly_payments.append(round(monthly_payment, 2))
		
			# ~ #Calculating the total amount to be repaid
			loan_repaid = monthly_payment * loan_duration
			total_loan_repaid.append(round(loan_repaid, 2))
		
			# ~ #Calculating the compound interest
			compound_interest = loan_amount * (1 + (interest_rate / 1)) ** (1 + loan_duration)
			compound_interests.append(round(compound_interest, 2))
			

			# ~ #Outputting the results
			print(
f"""For user {name} the total amount to be paid back is ${loan_repaid:,.2f},
the total amount to be paid back monthly is ${monthly_payment:,.2f} and
the compound interest on the loan is ${compound_interest:,.2f} 
			""")
			break
		else:
			print('ERROR: Please enter a valid response number.\n')
	
