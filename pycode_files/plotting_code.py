from PyQt5.QtWidgets import QMainWindow
from ui_files.plotting import Ui_Plotting
import numpy as np
from numpy import sin, cos, tan
from sympy import Symbol, simplify, SympifyError, lambdify


def ctg(x):
	return 1 / tan(x)


def asin(x):
	return 1 / sin(x)


def acos(x):
	return 1 / cos(x)


def atan(x):
	return 1 / tan(x)


def actg(x):
	return 1 / ctg(x)


class PlottingWidget(QMainWindow, Ui_Plotting):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.GraphicsView.setBackground('white')
		self.action_3.triggered.connect(self.open_usual_calculator)
		self.action_4.triggered.connect(self.open_engineering_calculator)
		self.action_6.triggered.connect(self.open_constants)
		
		self.expression = '0'
		self.allowed_values = '0123456789/*-+=()fx' + ''.join(set('sin cos tan ctg'))
		self.pushButton.clicked.connect(self.run)
		self.textEdit.textChanged.connect(self.expression_change)
	
	def expression_change(self):
		self.expression = "".join([
			*filter(lambda x: x in self.allowed_values, self.textEdit.toPlainText())
		])
	
	def run(self):
		try:
			self.GraphicsView.clear()
			self.x = Symbol('x')
			try:
				self.expression = simplify(self.expression[self.expression.index('=') + 1:])
			except SympifyError:
				self.textEdit.setText(f"could not parse {self.expression}")
			self.t = np.linspace(-20, 20, 30)
			self.eq = lambdify(self.x, self.expression)
			self.GraphicsView.plot(self.t, self.eq(self.t), pen='b')
		except Exception as e:
			print(e, type(e))
	
	def open_engineering_calculator(self):
		try:
			from pycode_files.engineering_calculator_code import EngineeringCalculator
			# To avoid cyclical imports
			self.engineering_calculator = EngineeringCalculator()
			self.engineering_calculator.show()
			self.close()
		except Exception as e:
			print(e)
	
	def open_usual_calculator(self):
		try:
			from pycode_files.usual_calculator_code import UsualCalculator
			# To avoid cyclical imports
			self.usual_calculator = UsualCalculator()
			self.usual_calculator.show()
			self.close()
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
