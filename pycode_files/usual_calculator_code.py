from PyQt5.QtWidgets import QMainWindow
from ui_files.common_calculator import Ui_UsualCalculatorWidget
from adapter_code import AdapterDB
from sqlite3 import OperationalError

adapter = AdapterDB('../results.db')


class UsualCalculator(QMainWindow, Ui_UsualCalculatorWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.expression = '0'
		self.ExpressionLabel.setText(self.expression)
		self.allowed_values = '0123456789()/*-+.'
		
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
		self.SquareRootButton.clicked.connect(self.square_root)
		
		# SpecialOperations
		self.DotButton.clicked.connect(self.add_dot)
		self.InverseButton.clicked.connect(self.inverse)
		self.NegativeButton.clicked.connect(self.negative)
		
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
		
		self.open_eng_calc_action.triggered.connect(self.open_engineering_calculator)
		self.open_plotting_action.triggered.connect(self.open_plotting)
		self.open_ph_const_action.triggered.connect(self.open_constants)
	
	def expression_change(self):
		self.expression = ''.join([
			*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())
		])
	
	def add_bracket(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + self.sender().text())
	
	def clear_all(self):
		self.ExpressionLabel.setText('0')
		self.ResultLabel.setText('')
		self.expression = '0'
	
	def delete(self):
		self.ExpressionLabel.setText(self.expression[:-1])
		self.ResultLabel.setText('')
		if not self.expression:
			self.ExpressionLabel.setText('0')
	
	def square_degree(self):
		self.ExpressionLabel.setText(self.expression + '**2')
	
	def square_root(self):
		self.ExpressionLabel.setText(self.expression + '**0.5')
	
	def add_operation(self):
		self.ExpressionLabel.setText(self.expression + self.sender().text())
	
	def inverse(self):
		try:
			self.expression = ''.join([*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())])
			self.result = f'{1 / eval(self.expression)}'
			self.ExpressionLabel.setText(self.result)
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
			self.ResultLabel.setText("Error")
			try:
				adapter.add_error(self.expression, er)
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
	
	def negative(self):
		if not self.expression:
			self.expression = '0'
		if '**2' not in self.expression and (
				'**0.5' not in self.expression) and (
				'*' not in self.expression) and (
				'-' not in self.expression) and (
				'-' not in self.expression) and (
				'/' not in self.expression):
			self.ExpressionLabel.setText(f"-{self.expression}")
		elif self.expression[0] == '-':
			self.ExpressionLabel.setText(self.expression[1:])
	
	def add_digit(self):
		if self.expression == '0':
			self.expression = ''
		self.ExpressionLabel.setText(self.expression + self.sender().text())
	
	def add_dot(self):
		if self.expression[-1] == '.':
			pass
		elif '.' in self.expression and (
				'*' not in self.expression) and (
				'-' not in self.expression) and (
				'-' not in self.expression) and (
				'/' not in self.expression):
			pass
		else:
			self.ExpressionLabel.setText(self.expression + self.sender().text())
	
	def calculate(self):
		try:
			self.expression = ''.join([*filter(lambda x: x in self.allowed_values, self.ExpressionLabel.toPlainText())])
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
			self.ResultLabel.setText("Error")
			try:
				adapter.add_error(self.expression, er)
			except OperationalError:
				adapter.add_error("", "Operation error with sql")
			
	def open_engineering_calculator(self):
		try:
			from pycode_files.engineering_calculator_code import EngineeringCalculator
			# To avoid cyclical imports
			self.engineering_calculator = EngineeringCalculator()
			self.engineering_calculator.show()
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
