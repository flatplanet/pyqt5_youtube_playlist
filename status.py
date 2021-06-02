from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.push_1())
        self.button1_pushButton.setGeometry(QtCore.QRect(10, 0, 230, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button1_pushButton.setFont(font)
        self.button1_pushButton.setObjectName("button1_pushButton")
        self.button2_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.push_2())
        self.button2_pushButton_2.setGeometry(QtCore.QRect(260, 0, 230, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button2_pushButton_2.setFont(font)
        self.button2_pushButton_2.setObjectName("button2_pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Change the statusbar font stuff
        self.statusbar.setFont(QFont('Times', 16))
        self.statusbar.showMessage("Ready...")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Status Bar Stuff"))
        self.button1_pushButton.setText(_translate("MainWindow", "Button 1"))
        self.button2_pushButton_2.setText(_translate("MainWindow", "Clear Status Bar"))

    def push_1(self):
        self.statusbar.showMessage("I Pressed Button 1!!!")

    def push_2(self):
        self.statusbar.showMessage("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
