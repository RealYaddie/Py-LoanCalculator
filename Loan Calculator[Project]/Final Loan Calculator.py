# Group Members: Vaughn Davis, Alexander Pinnock, Troy Hamilton, Leonard Smith
# Project Title: Loan Calculator
# Course: Computer Programming I
# Lecturer Name: Mr. Johnson

# This program is just a simple loan calculator that can calculate the monthly payment, the
# total amount to be paid back and the compound interest on the loan. The program should
# also give the option to display an amortization table based on the entered loan info.
#
# beautifultable module required

from beautifultable import BeautifulTable
import locale
locale.setlocale(locale.LC_ALL, '') # Sets the locale based on your language(LANG)
									# environment variable of your machine.


def amortize_schedule(amount, rate, payment_years):
    """This function is used to calculate an amortization schedule and displays
    a table showing all the payments, the changing loan amount with each
    payment, the principal, the remaining balance after each payment and the
    actual amount being paid each time.

    The function accepts three parameters:
    
    value: This is the loan amount borrowed.
    
    rate: This is the value of the interest rate that has already been 
           converted to the monthly interest rate.
           
    pmt_yrs: This represents the number of years given to repay the loan.
    """
    
    num_of_months = 0
    total_payments = payment_years * 12
    
    payment = (amount*(rate*(pow(1+rate, total_payments))))\
				/ (pow((1+rate), total_payments)-1)
				
    table = BeautifulTable()
    table.columns.header = ['PAYMENT NO.', 'LOAN VALUE', 'INTEREST', 'PRINCIPAL', 'PAYMENT', 'REMAINING BALANCE']

    while amount > 0:
        num_of_months += 1
        interest = (amount * rate)
        principal = payment - interest
        
        if amount - payment < 0:
            principal = amount
        table.rows.append([num_of_months,locale.currency(amount, grouping = 'yes'),
                           locale.currency(interest, grouping = 'yes'),
                           locale.currency(principal, grouping = 'yes'),
                           locale.currency(payment, grouping = 'yes'),
                           locale.currency(amount-principal, grouping = 'yes')])
        
        amount -= principal
        
    print(table)
    
    
def menu_check():
    '''
    The purpose of this function is to limit the user to only entering valid responses
    from a list provided.
    '''
    while True:
        try:
            user_input = int(input('Please choose a valid response from the list provided: '))
        except ValueError:
            print('ERROR: Please enter a valid reponse number. ')
            continue
        if user_input <= 0 or user_input > 4:
            print('ERROR: Please choose a valid response number!')
            continue
        else:
            return user_input
            
            
# Initializing lists to store information that the user enters
loan_amounts = []
interest_rates = []
loan_durations = []
monthly_payments = []
total_loan_repaid = []
compound_interests = []
counter = 0

# This while loop controls the heart of the program, the while loop keeps running until
# the user chooses one of the options that will end the program.
while True:
	print('''\n\tPlease choose from one of the list of valid input options below:
		\t1. If you\'re finished and wish to exit the program.
		\t2. If you wish to enter some loan information.
		\t3. If you\'d like to view the amortization table based on the information you last entered in the form of a table.
		\t4. This option displays the amortization table based on the information you entered last in a tabular format and ends the program.\n'''
		)
	option = menu_check()
	
	if option == 1:
		break

	# This option deals with the gathering of loan information from the user.
	elif option == 2:
		# The purpose of this loop is to ensure that the user is only able to enter 
        # numeric values for loan_amount, interest_rate and the loan_duration
		while True:
			try:
				# Getting the loan amount
				loan_amount = float(input("Enter the principal amount: "))
				loan_amounts.append(loan_amount)
				
				# Getting the interest rate
				interest_rate = float(input("Enter the interest rate on the loan amount: ")) / 100
				interest_rate = interest_rate / 12
				interest_rates.append(interest_rate)
				
				# Getting the loan duration
				loan_duration = float(input("Enter the number of years that you have to repay the loan: "))
				periods = loan_duration * 12
				loan_durations.append(loan_duration)
	
			except ValueError:
				print('ERROR: Please enter a valid response!')
				continue

			# Calculation section - In this section through the user of various formulae, the monthly payment,
			# the total amount to be repaid and the compound interest is calculated.
			monthly_payment = (loan_amount * (interest_rate * (pow((1 + interest_rate), periods)))) / ((pow((1 + interest_rate), periods) - 1))
			monthly_payments.append(round(monthly_payment, 2))

			loan_repaid = monthly_payment * loan_duration * 12
			total_loan_repaid.append(round(loan_repaid, 2))

			compound_interest = loan_amount * (1 + ((interest_rate * 12)/ 1)) ** (1 * loan_duration)
			compound_interests.append(round(compound_interest, 2))

			# Using a multi-line string to output the calculated amounts to the user
			print(f"""\nFor the loan amount of ${loan_amounts[counter]:,.2f}.
				\nThe total amount to be paid back is ${total_loan_repaid[counter]:,.2f},
				\nthe total amount to be paid back monthly is ${monthly_payments[counter]:,.2f} and
				\nthe compound interest on the loan is ${compound_interests[counter] - loan_amounts[counter]:,.2f}"""
				)
			counter += 1
			break
	
	# Using the loan info. an amortization table is outputted and the 
	# user is sent back to the start of the main loop
	elif option == 3:
		if counter == 0: # If the loop from above was not yet run.
			print('\nNo information was entered as yet...\n')
			continue
		amortize_schedule(loan_amount, interest_rate, loan_duration)
		continue
		
	# The same as option 3 but instead the program is terminated after.
	elif option == 4:
		if counter == 0:
			print('\nNo information to display...\n')
			continue
		amortize_schedule(loan_amount, interest_rate, loan_duration)
		break
