from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(120, 20, 105, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 70, 90, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(120, 120, 120, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 180, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set Button States
        self.radioButton.toggled.connect(lambda:self.btnstate(self.radioButton))
        self.radioButton_2.toggled.connect(lambda:self.btnstate(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda:self.btnstate(self.radioButton_3))

        #Set default radio button checked
        self.radioButton.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Peperoni"))
        self.radioButton_2.setText(_translate("MainWindow", "Cheese"))
        self.radioButton_3.setText(_translate("MainWindow", "Mushroom"))
        self.label.setText(_translate("MainWindow", "Choose Your Topping"))

    def btnstate(self, b):
        if b.isChecked():
            if b.text() == "Cheese":
                self.label.setText("I LOVE CHEESE!")    
            else:
                self.label.setText(b.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
