from PyQt5.QtWidgets import QWidget
from ui_files.physics_constants import Ui_PhConstants
from math import tau, pi, e

constants = {
	'ec': -1.602176620898 * 10 ** (-19),  # [Kl]
	'em': 9.109 * 10 ** (-31),  # [kg]
	'G': 6.67430152 * 10 ** (-11),  # [m ** 3 * kg ** (-1) * s ** (-2)]
	'g': 9.780,  # [m / s ** 2]
	'c': 299792458,  # [m / s]
	'h': 6.62607015 * 10 ** (-34),  # [J * s]
	'nA': 6.02214076 * 10 ** 23,  # [mol ** (-1)]
	'cB': 1.380649 * 10 ** (-23),  # [J * K ** (-1)]
	'mV': 22.41396954  # [l / mol]
	
}


class PhConstants(QWidget, Ui_PhConstants):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.ButtonE.clicked.connect(self.show_e)
		self.ButtonPi.clicked.connect(self.show_pi)
		self.ButtonTau.clicked.connect(self.show_tau)
		self.ButtonEC.clicked.connect(self.show_ec)
		self.ButtonEM.clicked.connect(self.show_em)
		self.ButtonGravitional.clicked.connect(self.show_g)
		self.ButtonAFF.clicked.connect(self.show_aff)
		self.ButtonSLL.clicked.connect(self.show_c)
		self.ButtonPC.clicked.connect(self.show_h)
		self.ButtonNAvogadro.clicked.connect(self.show_na)
		self.ButtonConstBoltzmann.clicked.connect(self.show_cb)
		self.ButtonMolarVolume.clicked.connect(self.show_mv)
	
	def passed(self):
		pass
	
	def show_pi(self):
		self.textBrowser.setText(f"{pi}")
	
	def show_e(self):
		self.textBrowser.setText(f"{e}")
	
	def show_tau(self):
		self.textBrowser.setText(f"{tau}")
	
	def show_ec(self):  # Electron charge
		self.textBrowser.setText(f"{constants.get('ec')}")
	
	def show_em(self):  # Electron mass
		self.textBrowser.setText(f"{constants.get('em')}")
	
	def show_g(self):  # Gravitational constant
		self.textBrowser.setText(f"{constants.get('G')}")
	
	def show_aff(self):  # Acceleration of free fall
		self.textBrowser.setText(f"{constants.get('g')}")
	
	def show_c(self):  # Speed of light
		self.textBrowser.setText(f"{constants.get('c')}")
	
	def show_h(self):  # Planck's constant
		self.textBrowser.setText(f"{constants.get('h')}")
	
	def show_na(self):  # Avogadro's number
		self.textBrowser.setText(f"{constants.get('nA')}")
	
	def show_cb(self):  # Boltzmann constant
		self.textBrowser.setText(f"{constants.get('cB')}")
	
	def show_mv(self):  # Molar Volume
		self.textBrowser.setText(f"{constants.get('mV')}")
	
	def open_usual_calculator(self):
		try:
			from pycode_files.usual_calculator_code import UsualCalculator
			# To avoid cyclical imports
			self.usual_calculator = UsualCalculator()
			self.usual_calculator.show()
			self.close()
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
	
	def open_plotting(self):
		try:
			from pycode_files.plotting_code import PlottingWidget
			# To avoid cyclical imports
			self.plotting_widget = PlottingWidget()
			self.plotting_widget.show()
			self.close()
		except Exception as e:
			print(e)