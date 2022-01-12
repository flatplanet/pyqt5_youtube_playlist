from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("text_bind.ui", self)
		self.setWindowTitle("Bind Text Typing") 

		# Define our widgets
		self.edit = self.findChild(QLineEdit, "lineEdit")
		self.label = self.findChild(QLabel, "label")

		# Hit Enter Button
		self.edit.editingFinished.connect(self.hitEnter)

		# On Click
		self.edit.textChanged.connect(self.changeText)

		# Show The App
		self.show()

	# Click Enter
	def hitEnter(self):
		self.label.setText(self.edit.text())

	# Change Text
	def changeText(self):
		self.label.setText(self.edit.text())


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

