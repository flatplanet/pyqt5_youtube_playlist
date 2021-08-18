from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def closeMain(self, main_w):
        main_w.hide()

    def showMain(self, main_w):
        main_w.show()
        main_w.pushButton_2.hide()

    def hideSecond(self, second_w):
        second_w.hide()


    def setupUi(self, SecondWindow, MainWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(543, 178)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.closeMain(MainWindow))
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.showMain(MainWindow))
        self.pushButton_2.setGeometry(QtCore.QRect(190, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.hideSecond(SecondWindow))
        self.pushButton_3.setGeometry(QtCore.QRect(370, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate("SecondWindow", "Type Something in the other Window!"))
        self.pushButton.setText(_translate("SecondWindow", "Hide Main"))
        self.pushButton_2.setText(_translate("SecondWindow", "Show Main"))
        self.pushButton_3.setText(_translate("SecondWindow", "Hide This One!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
