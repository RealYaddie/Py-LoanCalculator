import unittest
import formulas

loan_amount = 10000.0
interest_rate = 5.0
loan_duration = 3.0

class TestFormulas(unittest.TestCase):
	
	def test_monthly_four(self):
		loan_amount = 10000.0
		interest_rate = 5.0
		loan_duration = 3.0
		result = formulas.monthly_payment(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 299.71)
	
	def test_total_five(self):
		loan_amount = 10000.0
		interest_rate = 5.0
		loan_duration = 3.0
		result = formulas.total_amount(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 10789.52)
		
	def test_compound_six(self):
		loan_amount = 10000.0
		interest_rate = 5.0
		loan_duration = 3.0
		result = formulas.compound_interest(loan_amount, interest_rate, loan_duration)
		self.assertEqual(result, 1576.25)

if __name__ == '__main__':
	unittest.main()
