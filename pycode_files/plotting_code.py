from PyQt5.QtWidgets import QMainWindow
from ui_files.plotting import Ui_Plotting
from adapter_code import AdapterDB


class PlottingWidget(QMainWindow, Ui_Plotting):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.action_3.triggered.connect(self.open_usual_calculator)
		self.action_4.triggered.connect(self.open_engineering_calculator)
		self.action_6.triggered.connect(self.open_constants)
		
		self.expression = 'f(x) = x ** 2'
		self.allowed_values = '0123456789/*-+=()fx'
		self.pushButton.clicked.connect(self.run)
		self.textEdit.textChanged.connect(self.expression_change)
	
	def expression_change(self):
		self.expression = ''.join([
			*filter(lambda x: x in self.allowed_values, self.textEdit.toPlainText())
		])
		print(self.expression)
	
	def run(self):
		try:
			self.GraphicsView.clear()
			self.function = self.expression.replace(' ', '').split('=')[1]
			# f(x) = 3 * x ** 2
			self.zeros_func = []
			self.GraphicsView.plot([i for i in range(10)], [i ** 3 for i in range(10)], pen='b')
		except Exception as e:
			print(e)
	
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
