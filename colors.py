from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("colors.ui", self)

		# Add Menu Triggers
		self.actionBlack.triggered.connect(lambda: self.change("black"))
		self.actionWhite.triggered.connect(lambda: self.change("white"))
		self.actionRed.triggered.connect(lambda: self.change("red"))
		self.actionBlue.triggered.connect(lambda: self.change("blue"))
		self.actionGreen.triggered.connect(lambda: self.change("green"))
		self.actionYellow.triggered.connect(lambda: self.change("yellow"))


		
		# Show The App
		self.show()

	def change(self, color):
		# Change BG color
		self.setStyleSheet(f"background-color: {color};")
		# Change The Title
		self.setWindowTitle(f"You Changed The Color To {color}")


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


