def monthly_payment(amount, rate, periods):
	# ~ amount = amount
	rate = (rate/100)/12
	periods = periods*12
	monthly = (amount * (rate * (pow((1 + rate), periods)))) / ((pow((1 + rate), periods) - 1))
	return round(monthly, 2)
	
	
def total_amount(amount, rate, years):
	rate = (rate/100)/12
	periods = years*12
	monthly_pay = (amount * (rate * (pow((1 + rate), periods)))) / ((pow((1 + rate), periods) - 1))
	return round((monthly_pay*periods), 2)
	
	
def compound_interest(amount, rate, duration):
	rate = (rate/100)
	cmp_int = amount * (1 + ((rate)/ 1)) ** (1 * duration)
	return round((cmp_int-amount), 2)
	
	
# ~ print('Monthly payment -> ', monthly_payment(loan_amount, interest_rate, loan_duration))
# ~ print('\nTotal amount -> ', total_amount(loan_amount, interest_rate, loan_duration))
# ~ print('\nCompound Interest -> ', compound_interest(loan_amount, interest_rate, loan_duration))
