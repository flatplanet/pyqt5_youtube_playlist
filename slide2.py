from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider, QLabel
from PyQt5 import uic
from PyQt5 import QtCore
import sys


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("slide2.ui", self)
		self.setWindowTitle("Slider!") 

		# Define our widgets
		self.slider = self.findChild(QSlider, "horizontalSlider")
		self.label = self.findChild(QLabel, "label")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		
		self.slider.setMinimum(0)
		self.slider.setMaximum(50)
		self.slider.setValue(0)
		self.slider.setTickPosition(QSlider.TicksBelow)
		self.slider.setTickInterval(1)

		# Move The Slider
		#self.t_button.clicked.connect(self.translate)
		#self.slider.valueChanged[int].connect(self.slide_it)
		self.slider.valueChanged.connect(self.slide_it)
		# Show The App
		self.show()

	def slide_it(self, value):
		
		self.label.setText(str(value))
		

	

	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

