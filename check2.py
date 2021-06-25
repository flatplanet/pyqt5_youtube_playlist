from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(251, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(90, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setObjectName("red_checkBox")
        self.blue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(90, 70, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 251, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Update Check Boxes
        self.red_checkBox.stateChanged.connect(lambda:self.checked())
        self.blue_checkBox.toggled.connect(lambda:self.checked())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.label.setText(_translate("MainWindow", "Pick A Color"))

    def checked(self):
        if self.red_checkBox.isChecked() == True:
            self.red = "Red"
        else:
            self.red = ''

        if self.blue_checkBox.isChecked() == True:
            self.blue = "Blue"
        else:
            self.blue = ''

        self.label.setText(f'{self.red} {self.blue}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
