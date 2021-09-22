from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("toe.ui", self)

		# Define A Counter To Keep Track Of Who's Turn It IS
		self.counter = 0

		# Define our widgets
		self.button1 = self.findChild(QPushButton, "pushButton_1")
		self.button2 = self.findChild(QPushButton, "pushButton_2")
		self.button3 = self.findChild(QPushButton, "pushButton_3")
		self.button4 = self.findChild(QPushButton, "pushButton_4")
		self.button5 = self.findChild(QPushButton, "pushButton_5")
		self.button6 = self.findChild(QPushButton, "pushButton_6")
		self.button7 = self.findChild(QPushButton, "pushButton_7")
		self.button8 = self.findChild(QPushButton, "pushButton_8")
		self.button9 = self.findChild(QPushButton, "pushButton_9")
		self.button10 = self.findChild(QPushButton, "pushButton_10")
		self.label = self.findChild(QLabel, "label")

		# Click The Button
		self.button1.clicked.connect(lambda: self.clicker(self.button1))
		self.button2.clicked.connect(lambda: self.clicker(self.button2))
		self.button3.clicked.connect(lambda: self.clicker(self.button3))
		self.button4.clicked.connect(lambda: self.clicker(self.button4))
		self.button5.clicked.connect(lambda: self.clicker(self.button5))
		self.button6.clicked.connect(lambda: self.clicker(self.button6))
		self.button7.clicked.connect(lambda: self.clicker(self.button7))
		self.button8.clicked.connect(lambda: self.clicker(self.button8))
		self.button9.clicked.connect(lambda: self.clicker(self.button9))
		self.button10.clicked.connect(self.reset)
			

		# Show The App
		self.show()

	# Click The Buttons
	def clicker(self, b):
		if self.counter % 2 == 0:
			mark = "X"
			self.label.setText("O's Turn")
		else:
			mark = "O"
			self.label.setText("X's Turn")

		b.setText(mark)
		b.setEnabled(False)

		# Increment The Counter
		self.counter += 1


	# Start Over
	def reset(self):
		# Create a List of all our buttons
		button_list = [
		self.button1,
		self.button2,
		self.button3,
		self.button4,
		self.button5,
		self.button6,
		self.button7,
		self.button8,
		self.button9,]

		# Reset The Buttons
		for b in button_list:
			b.setText("")
			b.setEnabled(True)

		# Reset The Label
		self.label.setText("X Goes First!")

		# Reset The Counter
		self.counter = 0


	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

