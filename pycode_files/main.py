import sys

from PyQt5.QtWidgets import QApplication
from usual_calculator_code import UsualCalculator


if __name__ == '__main__':
	sys.set_int_max_str_digits(1000000000)
	app = QApplication(sys.argv)
	ex = UsualCalculator()
	ex.show()
	sys.exit(app.exec())
	