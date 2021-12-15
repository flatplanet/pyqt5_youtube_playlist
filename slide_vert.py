from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("slider_vert.ui", self)
		self.setWindowTitle("Slider!") 

		# Define our widgets
		self.slider = self.findChild(QSlider, "verticalSlider")
		self.label = self.findChild(QLabel, "label")
		
		# Set Slider Properties
		self.slider.setMinimum(0)
		self.slider.setMaximum(50)
		self.slider.setValue(0)
		self.slider.setTickPosition(QSlider.TicksLeft)
		self.slider.setTickInterval(5)
		self.slider.setSingleStep(5)

		# Move The Slider
		self.slider.valueChanged.connect(self.slide_it)


		# Show The App
		self.show()

	def slide_it(self, value):
		self.label.setText(str(value))


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


