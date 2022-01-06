from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("hide.ui", self)
		self.setWindowTitle("Hide And Unhide Things") 

		# Define our widgets
		self.edit = self.findChild(QLineEdit, "lineEdit")
		self.button = self.findChild(QPushButton, "pushButton")
		
		# Click the buttons
		self.button.clicked.connect(self.hide_unhide)

		# Show The App
		self.show()

		# Keep Track of hidden or not
		self.hidden = False

	def hide_unhide(self):
		if self.hidden:
			self.edit.show()
			self.hidden = False
		else:
			self.edit.hide()
			self.hidden = True


	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

