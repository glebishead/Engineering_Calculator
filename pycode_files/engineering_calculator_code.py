from PyQt5.QtWidgets import QMainWindow
from ui_files.engineering_calculator import Ui_EngineeringCalculatorWidget
from adapter_code import AdapterDB
from sqlite3 import OperationalError
from math import tan, e, pi, asin, acos, atan, log, factorial as fact, radians as rad
from numpy import sin, cos, tan


def ctg(n):
	return 1 / tan(n)


def actg(n):
	return 1 / ctg(n)


adapter = AdapterDB('../results.db')


class EngineeringCalculator(QMainWindow, Ui_EngineeringCalculatorWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.expression = '0'
		self.ExpressionLabel.setText(self.expression)
		self.allowed_values = '0123456789-+*/(),.' + ''.join(set('sincostanctgactgradlogfactabs'))
		
		self.ExpressionLabel.textChanged.connect(self.expression_change)
		
		# ClearOperations
		self.ClearAllButton.clicked.connect(self.clear_all)
		self.DeleteButton.clicked.connect(self.delete)
		
		# ArithmeticOperations
		self.PlusButton.clicked.connect(self.add_operation)
		self.MinusButton.clicked.connect(self.add_operation)
		self.MultiplicationButton.clicked.connect(self.add_operation)
		self.DivisionButton.clicked.connect(self.add_operation)
		self.SecondDegreeButton.clicked.connect(self.square_degree)
		self.ThirdDegreeButton.clicked.connect(self.cubic_degree)
		self.NDegreeButton.clicked.connect(self.n_degree)
		self.SquareRootButton.clicked.connect(self.square_root)
		self.CubicRootButton.clicked.connect(self.cubic_root)
		self.NRootButton.clicked.connect(self.n_root)
		
		# Constants
		self.ButtonE.clicked.connect(self.add_e)
		self.ButtonPi.clicked.connect(self.add_pi)
		
		# Trigonometric
		self.SineButton.clicked.connect(self.sine)
		self.CosineButton.clicked.connect(self.cosine)
		self.TangentButton.clicked.connect(self.tangent)
		self.CotangenceButton.clicked.connect(self.cotangent)
		self.ArcsineButton.clicked.connect(self.asine)
		self.ArccosineButton.clicked.connect(self.acosine)
		self.ArctangentButton.clicked.connect(self.atangent)
		self.ArcCotangenceButton.clicked.connect(self.acotangent)
		
		# SpecialOperations
		self.DotButton.clicked.connect(self.add_dot)
		self.InverseButton.clicked.connect(self.inverse)
		self.MultiplicationTenDegreeNButton.clicked.connect(self.mult_ten_degree)
		self.FactorialButton.clicked.connect(self.fact)
		self.ModuleButton.clicked.connect(self.mod)
		self.LogarithmButton.clicked.connect(self.logarithm)
		self.NaturalLogarithmE.clicked.connect(self.natural_logarithm)
		
		# BracketsButtons
		self.LeftBracketButton.clicked.connect(self.add_bracket)
		self.RightBracketButton.clicked.connect(self.add_bracket)
		
		# DigitButtons
		self.OneButton.clicked.connect(self.add_digit)
		self.TwoButton.clicked.connect(self.add_digit)
		self.ThreeButton.clicked.connect(self.add_digit)
		self.FourButton.clicked.connect(self.add_digit)
		self.FiveButton.clicked.connect(self.add_digit)
		self.SixButton.clicked.connect(self.add_digit)
		self.SevenButton.clicked.connect(self.add_digit)
		self.EightButton.clicked.connect(self.add_digit)
		self.NineButton.clicked.connect(self.add_digit)
		self.ZeroButton.clicked.connect(self.add_digit)
		
		# Calculate
		self.EqualsButton.clicked.connect(self.calculate)
		
		self.open_common_calc_action.triggered.connect(self.open_usual_calculator)
		self.open_plotting_action.triggered.connect(self.open_plotting)
		self.open_ph_const_action.triggered.connect(self.open_constants)
	
	def expression_change(self):
		self.expression = ''.join([*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())])
	
	def add_bracket(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + self.sender().text())
	
	def clear_all(self):
		self.ExpressionLabel.setText('0')
		self.ResultLabel.setText('')

	def delete(self):
		if len(self.expression) > 1:
			self.ExpressionLabel.setText(self.expression[:-1])
		else:
			self.ExpressionLabel.setText('0')

	def square_degree(self):
		self.ExpressionLabel.setText(self.expression + '**2')
	
	def cubic_degree(self):
		self.ExpressionLabel.setText(self.expression + '**3')
	
	def n_degree(self):
		self.ExpressionLabel.setText(self.expression + '**(n)')
	
	def square_root(self):
		self.ExpressionLabel.setText(self.expression + '**(0.5)')
	
	def cubic_root(self):
		self.ExpressionLabel.setText(self.expression + '**(1/3)')
	
	def n_root(self):
		self.ExpressionLabel.setText(self.expression + '**(1/n)')
	
	def add_operation(self):
		if self.expression[-1] in '+-*/':
			self.expression = self.expression[:-1]
		self.ExpressionLabel.setText(self.expression + f'{self.sender().text()}')
	
	def add_e(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + f'{e}')
	
	def add_pi(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + f'{pi}')
	
	def sine(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'sin(')
	
	def cosine(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'cos(')
	
	def tangent(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'tan(')
	
	def cotangent(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'ctg(')
	
	def asine(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'asin(')
	
	def acosine(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'acos(')
	
	def atangent(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'atan(')
	
	def acotangent(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'actg(')
	
	def fact(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'fact(')
	
	def mod(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'abs(')
	
	def logarithm(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + 'log(n, b)')
	
	def natural_logarithm(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + f'log(n, {e})')
	
	def inverse(self):
		try:
			self.expression = ''.join([*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())])
			self.result = f"{1 / eval(self.expression)}"
			self.ResultLabel.setText(f"{self.result}")
			try:
				adapter.add_result(self.expression, self.result)
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
		except ZeroDivisionError:
			self.ResultLabel.setText("Division by zero")
			try:
				adapter.add_error(self.expression, "Division by zero")
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
		except Exception as er:
			try:
				if er.__class__.__name__ == 'ValueError':
					self.ResultLabel.setText('Math domain error')
				else:
					self.ResultLabel.setText("Wrong data")
				adapter.add_error(self.expression, er)
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
	
	def mult_ten_degree(self):
		self.ExpressionLabel.setText(self.expression + '*10**(n)')
	
	def add_digit(self):
		try:
			if self.expression == '0':
				self.expression = ''
			elif self.expression == '-0':
				self.expression = '-'
			self.ExpressionLabel.setText(self.expression + self.sender().text())
		except Exception as e:
			print(e)
	
	def add_dot(self):
		if self.expression[-1] == '.' or self.expression[-1] in '*-+/':
			pass
		else:
			self.ExpressionLabel.setText(self.expression + '.')
	
	def calculate(self):
		try:
			if self.DegRadioButton.isChecked():
				if 'sin(rad(' not in self.expression and 'sin(' in self.expression:
					self.ExpressionLabel.setText(self.expression.replace('sin(', 'sin(rad('))
				elif 'cos(rad(' not in self.expression and 'cos(' in self.expression:
					self.ExpressionLabel.setText(self.expression.replace('cos(', 'cos(rad('))
				elif 'tan(rad(' not in self.expression and 'tan(' in self.expression:
					self.ExpressionLabel.setText(self.expression.replace('tan(', 'tan(rad('))
				elif 'ctg(rad(' not in self.expression and 'ctg(' in self.expression:
					self.ExpressionLabel.setText(self.expression.replace('ctg(', 'ctg(rad('))
		
			if 'sin(rad(90))' in self.expression:
				self.expression = self.expression.replace('sin(rad(90))', '1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(3.141592653589793/2)' in self.expression:
				self.expression = self.expression.replace('sin(3.141592653589793/2)', '1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(1.5707963267948966)' in self.expression:
				self.expression = self.expression.replace('sin(1.5707963267948966)', '1')
				self.ExpressionLabel.setText(self.expression)

			if 'cos(rad(90))' in self.expression:
				self.expression = self.expression.replace('cos(rad(90))', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(3.141592653589793/2)' in self.expression:
				self.expression = self.expression.replace('cos(3.141592653589793/2)', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(1.5707963267948966)' in self.expression:
				self.expression = self.expression.replace('cos(1.5707963267948966)', '0')
				self.ExpressionLabel.setText(self.expression)
			
			if 'sin(rad(180))' in self.expression:
				self.expression = self.expression.replace('sin(rad(180))', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('sin(3.141592653589793)', '0')
				self.ExpressionLabel.setText(self.expression)
			
			if 'cos(rad(180))' in self.expression:
				self.expression = self.expression.replace('cos(rad(180))', '-1')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('cos(3.141592653589793)', '-1')
				self.ExpressionLabel.setText(self.expression)
			
			if 'sin(rad(270))' in self.expression:
				self.expression = self.expression.replace('sin(rad(270))', '-1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(3*3.141592653589793/2)' in self.expression:
				self.expression = self.expression.replace('sin(3*3.141592653589793/2)', '-1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(3.141592653589793*3/2)' in self.expression:
				self.expression = self.expression.replace('sin(3.141592653589793*3/2)', '-1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(3.141592653589793/2*3)' in self.expression:
				self.expression = self.expression.replace('sin(3.141592653589793/2*3)', '-1')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(4.71238898038469)' in self.expression:
				self.expression = self.expression.replace('sin(4.71238898038469)', '-1')
				self.ExpressionLabel.setText(self.expression)
			
			if 'cos(rad(270))' in self.expression:
				self.expression = self.expression.replace('cos(rad(270))', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(3*3.141592653589793/2)' in self.expression:
				self.expression = self.expression.replace('cos(3*3.141592653589793/2)', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(3.141592653589793*3/2)' in self.expression:
				self.expression = self.expression.replace('cos(3.141592653589793*3/2)', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(3.141592653589793/2*3)' in self.expression:
				self.expression = self.expression.replace('cos(3.141592653589793/2*3)', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(4.71238898038469)' in self.expression:
				self.expression = self.expression.replace('cos(4.71238898038469)', '0')
				self.ExpressionLabel.setText(self.expression)
			
			if 'sin(rad(360))' in self.expression:
				self.expression = self.expression.replace('sin(rad(360))', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(2*3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('sin(2*3.141592653589793)', '0')
				self.ExpressionLabel.setText(self.expression)
			if 'sin(2*3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('sin(2*3.141592653589793)', '0')
				self.ExpressionLabel.setText(self.expression)
			
			if 'cos(rad(360))' in self.expression:
				self.expression = self.expression.replace('cos(rad(360))', '1')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(2*3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('cos(2*3.141592653589793)', '1')
				self.ExpressionLabel.setText(self.expression)
			if 'cos(2*3.141592653589793)' in self.expression:
				self.expression = self.expression.replace('cos(2*3.141592653589793)', '1')
				self.ExpressionLabel.setText(self.expression)
			
			if 'tan(rad(90))' in self.expression or 'tan(rad(270))' in self.expression:
				self.ExpressionLabel.setText('')
				self.ResultLabel.setText('Does not exists')
			
			if 'ctg(rad(180))' in self.expression or 'ctg(rad(360))' in self.expression:
				self.ExpressionLabel.setText('')
				self.ResultLabel.setText('Does not exists')
			
			if 'tan(3.141592653589793/2)' in self.expression or 'tan(1.5707963267948966)' in self.expression:
				self.ExpressionLabel.setText('')
				self.ResultLabel.setText('Does not exists')
			
			if 'tan(3*3.141592653589793/2)' in self.expression or (
					'tan(3.141592653589793*3/2)' in self.expression) or (
					'tan(3.141592653589793/2*3)' in self.expression):
				self.ExpressionLabel.setText('')
				self.ResultLabel.setText('Does not exists')
			
			if 'ctg(3.141592653589793)' in self.expression or (
					'ctg(2*3.141592653589793)' in self.expression) or (
					'ctg(3.141592653589793*2)' in self.expression):
				self.ExpressionLabel.setText('')
				self.ResultLabel.setText('Does not exists')
			
			if self.ResultLabel.toPlainText() != 'Does not exists':
				self.expression = ''.join(
					[*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())]
				)
				self.result = eval(self.expression)
				self.ResultLabel.setText(f"{self.result}")
			try:
				adapter.add_result(self.expression, f'{self.result}')
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
		except ZeroDivisionError:
			self.ResultLabel.setText("Division by zero")
			try:
				adapter.add_error(self.expression, "Division by zero")
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
		except Exception as er:
			try:
				if er.__class__.__name__ == 'ValueError':
					self.ResultLabel.setText('Math domain error')
				else:
					self.ResultLabel.setText("Wrong data")
				adapter.add_error(self.expression, er)
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
	
	def open_usual_calculator(self):
		try:
			from pycode_files.usual_calculator_code import UsualCalculator
			# To avoid cyclical imports
			self.usual_calculator = UsualCalculator()
			self.usual_calculator.show()
			self.close()
			adapter.close_db()
		except Exception as e:
			print(e)
			
	def open_plotting(self):
		try:
			from pycode_files.plotting_code import PlottingWidget
			# To avoid cyclical imports
			self.plotting_widget = PlottingWidget()
			self.plotting_widget.show()
			self.close()
			adapter.close_db()
		except Exception as e:
			print(e)
	
	def open_constants(self):
		try:
			from pycode_files.PhConatsnts_code import PhConstants
			# To avoid cyclical imports
			self.ph_constants = PhConstants()
			self.ph_constants.show()
		except Exception as e:
			print(e)
