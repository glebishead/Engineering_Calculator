# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'engineering_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EngineeringCalculatorWidget(object):
    def setupUi(self, EngineeringCalculatorWidget):
        EngineeringCalculatorWidget.setObjectName("EngineeringCalculatorWidget")
        EngineeringCalculatorWidget.setWindowModality(QtCore.Qt.WindowModal)
        EngineeringCalculatorWidget.setEnabled(True)
        EngineeringCalculatorWidget.resize(491, 532)
        self.centralwidget = QtWidgets.QWidget(EngineeringCalculatorWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.ResultLabel = QtWidgets.QTextBrowser(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(0, 0, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setObjectName("ResultLabel")
        self.ExpressionLabel = QtWidgets.QTextEdit(self.centralwidget)
        self.ExpressionLabel.setGeometry(QtCore.QRect(0, 70, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ExpressionLabel.setFont(font)
        self.ExpressionLabel.setObjectName("ExpressionLabel")
        self.ButtonE = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonE.setGeometry(QtCore.QRect(280, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonE.setFont(font)
        self.ButtonE.setObjectName("ButtonE")
        self.DotButton = QtWidgets.QPushButton(self.centralwidget)
        self.DotButton.setGeometry(QtCore.QRect(350, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DotButton.setFont(font)
        self.DotButton.setObjectName("DotButton")
        self.SineButton = QtWidgets.QPushButton(self.centralwidget)
        self.SineButton.setGeometry(QtCore.QRect(70, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SineButton.setFont(font)
        self.SineButton.setObjectName("SineButton")
        self.OneButton = QtWidgets.QPushButton(self.centralwidget)
        self.OneButton.setGeometry(QtCore.QRect(210, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OneButton.setFont(font)
        self.OneButton.setObjectName("OneButton")
        self.ButtonPi = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPi.setGeometry(QtCore.QRect(210, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ButtonPi.setFont(font)
        self.ButtonPi.setObjectName("ButtonPi")
        self.LeftBracketButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftBracketButton.setGeometry(QtCore.QRect(280, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LeftBracketButton.setFont(font)
        self.LeftBracketButton.setObjectName("LeftBracketButton")
        self.CotangenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.CotangenceButton.setGeometry(QtCore.QRect(70, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CotangenceButton.setFont(font)
        self.CotangenceButton.setObjectName("CotangenceButton")
        self.NDegreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.NDegreeButton.setGeometry(QtCore.QRect(140, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NDegreeButton.setFont(font)
        self.NDegreeButton.setObjectName("NDegreeButton")
        self.SecondDegreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SecondDegreeButton.setGeometry(QtCore.QRect(140, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecondDegreeButton.setFont(font)
        self.SecondDegreeButton.setObjectName("SecondDegreeButton")
        self.SevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.SevenButton.setGeometry(QtCore.QRect(210, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SevenButton.setFont(font)
        self.SevenButton.setObjectName("SevenButton")
        self.FiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.FiveButton.setGeometry(QtCore.QRect(280, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FiveButton.setFont(font)
        self.FiveButton.setObjectName("FiveButton")
        self.CosineButton = QtWidgets.QPushButton(self.centralwidget)
        self.CosineButton.setGeometry(QtCore.QRect(70, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CosineButton.setFont(font)
        self.CosineButton.setObjectName("CosineButton")
        self.ArccosineButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArccosineButton.setGeometry(QtCore.QRect(0, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ArccosineButton.setFont(font)
        self.ArccosineButton.setObjectName("ArccosineButton")
        self.ThirdDegreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ThirdDegreeButton.setGeometry(QtCore.QRect(140, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ThirdDegreeButton.setFont(font)
        self.ThirdDegreeButton.setObjectName("ThirdDegreeButton")
        self.ArctangentButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArctangentButton.setGeometry(QtCore.QRect(0, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ArctangentButton.setFont(font)
        self.ArctangentButton.setObjectName("ArctangentButton")
        self.NineButton = QtWidgets.QPushButton(self.centralwidget)
        self.NineButton.setGeometry(QtCore.QRect(350, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NineButton.setFont(font)
        self.NineButton.setObjectName("NineButton")
        self.TangentButton = QtWidgets.QPushButton(self.centralwidget)
        self.TangentButton.setGeometry(QtCore.QRect(70, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TangentButton.setFont(font)
        self.TangentButton.setObjectName("TangentButton")
        self.EqualsButton = QtWidgets.QPushButton(self.centralwidget)
        self.EqualsButton.setGeometry(QtCore.QRect(420, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EqualsButton.setFont(font)
        self.EqualsButton.setObjectName("EqualsButton")
        self.PlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusButton.setGeometry(QtCore.QRect(420, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PlusButton.setFont(font)
        self.PlusButton.setObjectName("PlusButton")
        self.ArcCotangenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArcCotangenceButton.setGeometry(QtCore.QRect(0, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ArcCotangenceButton.setFont(font)
        self.ArcCotangenceButton.setObjectName("ArcCotangenceButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(420, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ThreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ThreeButton.setGeometry(QtCore.QRect(350, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ThreeButton.setFont(font)
        self.ThreeButton.setObjectName("ThreeButton")
        self.CubicRootButton = QtWidgets.QPushButton(self.centralwidget)
        self.CubicRootButton.setGeometry(QtCore.QRect(140, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CubicRootButton.setFont(font)
        self.CubicRootButton.setObjectName("CubicRootButton")
        self.EightButton = QtWidgets.QPushButton(self.centralwidget)
        self.EightButton.setGeometry(QtCore.QRect(280, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EightButton.setFont(font)
        self.EightButton.setObjectName("EightButton")
        self.SixButton = QtWidgets.QPushButton(self.centralwidget)
        self.SixButton.setGeometry(QtCore.QRect(350, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SixButton.setFont(font)
        self.SixButton.setObjectName("SixButton")
        self.TwoButton = QtWidgets.QPushButton(self.centralwidget)
        self.TwoButton.setGeometry(QtCore.QRect(280, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TwoButton.setFont(font)
        self.TwoButton.setObjectName("TwoButton")
        self.NRootButton = QtWidgets.QPushButton(self.centralwidget)
        self.NRootButton.setGeometry(QtCore.QRect(140, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NRootButton.setFont(font)
        self.NRootButton.setObjectName("NRootButton")
        self.FourButton = QtWidgets.QPushButton(self.centralwidget)
        self.FourButton.setGeometry(QtCore.QRect(210, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FourButton.setFont(font)
        self.FourButton.setObjectName("FourButton")
        self.MultiplicationButton = QtWidgets.QPushButton(self.centralwidget)
        self.MultiplicationButton.setGeometry(QtCore.QRect(420, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MultiplicationButton.setFont(font)
        self.MultiplicationButton.setObjectName("MultiplicationButton")
        self.SquareRootButton = QtWidgets.QPushButton(self.centralwidget)
        self.SquareRootButton.setGeometry(QtCore.QRect(140, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SquareRootButton.setFont(font)
        self.SquareRootButton.setObjectName("SquareRootButton")
        self.MinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.MinusButton.setGeometry(QtCore.QRect(420, 310, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MinusButton.setFont(font)
        self.MinusButton.setObjectName("MinusButton")
        self.ArcsineButton = QtWidgets.QPushButton(self.centralwidget)
        self.ArcsineButton.setGeometry(QtCore.QRect(0, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ArcsineButton.setFont(font)
        self.ArcsineButton.setObjectName("ArcsineButton")
        self.ZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZeroButton.setGeometry(QtCore.QRect(210, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ZeroButton.setFont(font)
        self.ZeroButton.setObjectName("ZeroButton")
        self.DivisionButton = QtWidgets.QPushButton(self.centralwidget)
        self.DivisionButton.setGeometry(QtCore.QRect(420, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DivisionButton.setFont(font)
        self.DivisionButton.setObjectName("DivisionButton")
        self.ClearAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearAllButton.setGeometry(QtCore.QRect(350, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClearAllButton.setFont(font)
        self.ClearAllButton.setObjectName("ClearAllButton")
        self.RightBracketButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightBracketButton.setGeometry(QtCore.QRect(350, 430, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RightBracketButton.setFont(font)
        self.RightBracketButton.setObjectName("RightBracketButton")
        self.InverseButton = QtWidgets.QPushButton(self.centralwidget)
        self.InverseButton.setGeometry(QtCore.QRect(280, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InverseButton.setFont(font)
        self.InverseButton.setObjectName("InverseButton")
        self.MultiplicationTenDegreeNButton = QtWidgets.QPushButton(self.centralwidget)
        self.MultiplicationTenDegreeNButton.setGeometry(QtCore.QRect(210, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MultiplicationTenDegreeNButton.setFont(font)
        self.MultiplicationTenDegreeNButton.setObjectName("MultiplicationTenDegreeNButton")
        self.FactorialButton = QtWidgets.QPushButton(self.centralwidget)
        self.FactorialButton.setGeometry(QtCore.QRect(70, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FactorialButton.setFont(font)
        self.FactorialButton.setObjectName("FactorialButton")
        self.LogarithmButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogarithmButton.setGeometry(QtCore.QRect(0, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LogarithmButton.setFont(font)
        self.LogarithmButton.setObjectName("LogarithmButton")
        self.ModuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ModuleButton.setGeometry(QtCore.QRect(70, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ModuleButton.setFont(font)
        self.ModuleButton.setObjectName("ModuleButton")
        self.NaturalLogarithmE = QtWidgets.QPushButton(self.centralwidget)
        self.NaturalLogarithmE.setGeometry(QtCore.QRect(0, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NaturalLogarithmE.setFont(font)
        self.NaturalLogarithmE.setObjectName("NaturalLogarithmE")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 82, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 0, 41, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        EngineeringCalculatorWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EngineeringCalculatorWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        EngineeringCalculatorWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EngineeringCalculatorWidget)
        self.statusbar.setObjectName("statusbar")
        EngineeringCalculatorWidget.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(EngineeringCalculatorWidget)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(EngineeringCalculatorWidget)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(EngineeringCalculatorWidget)
        self.action_7.setObjectName("action_7")
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(EngineeringCalculatorWidget)
        QtCore.QMetaObject.connectSlotsByName(EngineeringCalculatorWidget)

    def retranslateUi(self, EngineeringCalculatorWidget):
        _translate = QtCore.QCoreApplication.translate
        EngineeringCalculatorWidget.setWindowTitle(_translate("EngineeringCalculatorWidget", "Инженерный калькулятор"))
        self.ExpressionLabel.setHtml(_translate("EngineeringCalculatorWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ButtonE.setText(_translate("EngineeringCalculatorWidget", "e"))
        self.DotButton.setText(_translate("EngineeringCalculatorWidget", "."))
        self.SineButton.setText(_translate("EngineeringCalculatorWidget", "sin"))
        self.OneButton.setText(_translate("EngineeringCalculatorWidget", "1"))
        self.ButtonPi.setText(_translate("EngineeringCalculatorWidget", "𝞹"))
        self.LeftBracketButton.setText(_translate("EngineeringCalculatorWidget", "("))
        self.CotangenceButton.setText(_translate("EngineeringCalculatorWidget", "ctg"))
        self.NDegreeButton.setText(_translate("EngineeringCalculatorWidget", "xⁿ"))
        self.SecondDegreeButton.setText(_translate("EngineeringCalculatorWidget", "x²"))
        self.SevenButton.setText(_translate("EngineeringCalculatorWidget", "7"))
        self.FiveButton.setText(_translate("EngineeringCalculatorWidget", "5"))
        self.CosineButton.setText(_translate("EngineeringCalculatorWidget", "cos"))
        self.ArccosineButton.setText(_translate("EngineeringCalculatorWidget", "acos"))
        self.ThirdDegreeButton.setText(_translate("EngineeringCalculatorWidget", "x³"))
        self.ArctangentButton.setText(_translate("EngineeringCalculatorWidget", "atg"))
        self.NineButton.setText(_translate("EngineeringCalculatorWidget", "9"))
        self.TangentButton.setText(_translate("EngineeringCalculatorWidget", "tg"))
        self.EqualsButton.setText(_translate("EngineeringCalculatorWidget", "="))
        self.PlusButton.setText(_translate("EngineeringCalculatorWidget", "+"))
        self.ArcCotangenceButton.setText(_translate("EngineeringCalculatorWidget", "actg"))
        self.DeleteButton.setText(_translate("EngineeringCalculatorWidget", "Delete"))
        self.ThreeButton.setText(_translate("EngineeringCalculatorWidget", "3"))
        self.CubicRootButton.setText(_translate("EngineeringCalculatorWidget", "³√x"))
        self.EightButton.setText(_translate("EngineeringCalculatorWidget", "8"))
        self.SixButton.setText(_translate("EngineeringCalculatorWidget", "6"))
        self.TwoButton.setText(_translate("EngineeringCalculatorWidget", "2"))
        self.NRootButton.setText(_translate("EngineeringCalculatorWidget", "ⁿ√x"))
        self.FourButton.setText(_translate("EngineeringCalculatorWidget", "4"))
        self.MultiplicationButton.setText(_translate("EngineeringCalculatorWidget", "*"))
        self.SquareRootButton.setText(_translate("EngineeringCalculatorWidget", "√x"))
        self.MinusButton.setText(_translate("EngineeringCalculatorWidget", "-"))
        self.ArcsineButton.setText(_translate("EngineeringCalculatorWidget", "asin"))
        self.ZeroButton.setText(_translate("EngineeringCalculatorWidget", "0"))
        self.DivisionButton.setText(_translate("EngineeringCalculatorWidget", "/"))
        self.ClearAllButton.setText(_translate("EngineeringCalculatorWidget", "Clear"))
        self.RightBracketButton.setText(_translate("EngineeringCalculatorWidget", ")"))
        self.InverseButton.setText(_translate("EngineeringCalculatorWidget", "1/x"))
        self.MultiplicationTenDegreeNButton.setText(_translate("EngineeringCalculatorWidget", "×10ⁿ"))
        self.FactorialButton.setText(_translate("EngineeringCalculatorWidget", "!"))
        self.LogarithmButton.setText(_translate("EngineeringCalculatorWidget", "log"))
        self.ModuleButton.setText(_translate("EngineeringCalculatorWidget", "Mod"))
        self.NaturalLogarithmE.setText(_translate("EngineeringCalculatorWidget", "In"))
        self.radioButton.setText(_translate("EngineeringCalculatorWidget", "Deg"))
        self.radioButton_2.setText(_translate("EngineeringCalculatorWidget", "Rad"))
        self.menu.setTitle(_translate("EngineeringCalculatorWidget", "Инженерный калькулятор"))
        self.action_3.setText(_translate("EngineeringCalculatorWidget", "Обычный калькулятор"))
        self.action_5.setText(_translate("EngineeringCalculatorWidget", "Физические величины"))
        self.action_7.setText(_translate("EngineeringCalculatorWidget", "Построение графиков"))