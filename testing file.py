import unittest
import formulas

class TestFormulas(unittest.TestCase):
	#First Test Case
	def test_monthly_one(self):
		loan_amount = 1000.0
		interest_rate = 10.0
		loan_duration = 10.0
		result = formulas.monthly_payment(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 13.22)
	
	def test_total_two(self):
		loan_amount = 1000.0
		interest_rate = 10.0
		loan_duration = 10.0
		result = formulas.total_amount(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 1585.81)
		
	def test_compound_three(self):
		loan_amount = 1000.0
		interest_rate = 10.0
		loan_duration = 10.0
		result = formulas.compound_interest(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 1593.74)
	
	#Second Test Case
	def test_monthly_four(self):
		loan_amount = 100000.0
		interest_rate = 5.0
		loan_duration = 10.0
		result = formulas.monthly_payment(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 1060.66)
	
	def test_total_five(self):
		loan_amount = 100000.0
		interest_rate = 5.0
		loan_duration = 10.0
		result = formulas.total_amount(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 127278.62)
		
	def test_compound_six(self):
		loan_amount = 100000.0
		interest_rate = 5.0
		loan_duration = 10.0
		result = formulas.compound_interest(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 62889.46)
			
if __name__ == '__main__':
	unittest.main()
