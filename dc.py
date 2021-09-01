from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("dc.ui", self)

		# Define Our Widgets
		self.combo1 = self.findChild(QComboBox, "comboBox") 
		self.combo2 = self.findChild(QComboBox, "comboBox_2")
		self.label = self.findChild(QLabel, "label")

		# Add Items To The Dropdown boxes
		self.combo1.addItem("Male", ["John", "Wes", "Dan"])
		self.combo1.addItem("Female", ["April", "Steph", "Beth"])

		# Click First Dropdown Box
		self.combo1.activated.connect(self.clicker)
		self.combo2.activated.connect(self.clicker2)
		
		# Show The App
		self.show()

	def clicker(self, index):
		# Clear the second box
		self.combo2.clear()
		# Do the dependant thing
		self.combo2.addItems(self.combo1.itemData(index))

	def clicker2(self):
		self.label.setText(f'You Picked: {self.combo2.currentText()} - {self.combo1.currentText()}')
		
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

