from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("loadui.ui", self)

		# Define Our Widgets
		self.label = self.findChild(QLabel, "label")
		self.textedit = self.findChild(QTextEdit, "textEdit")
		self.button = self.findChild(QPushButton, "pushButton")
		self.clear_button = self.findChild(QPushButton, "pushButton_2")

		# Do something
		self.button.clicked.connect(self.clicker)
		self.clear_button.clicked.connect(self.clearer)

		# Show The App
		self.show()

	def clearer(self):
		self.textedit.setPlainText("")
		self.label.setText("Enter Your Name...")
		
	def clicker(self):
		self.label.setText(f'Hello There {self.textedit.toPlainText()}')
		self.textedit.setPlainText("")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

