from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("cal.ui", self)

		# Define our widgets
		self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
		self.label = self.findChild(QLabel, "label")

		# Connect the calendar to the function
		self.calendar.selectionChanged.connect(self.grab_date)

		# Show The App
		self.show()


	def grab_date(self):
		dateSelected = self.calendar.selectedDate()

		# Put Date On Label
		#self.label.setText(str(dateSelected.toPyDate()))
		self.label.setText(str(dateSelected.toString()))



# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


