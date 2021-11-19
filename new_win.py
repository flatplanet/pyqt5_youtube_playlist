from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
	count = 0
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("new_win.ui", self)

		# Define our widgets QPushButton
		self.mdi = self.findChild(QMdiArea, "mdiArea")
		self.button = self.findChild(QPushButton, "pushButton")
		

		# Click Button
		self.button.clicked.connect(self.add_window)

		# Show The App
		self.show()

	def add_window(self):
		UI.count = UI.count + 1
		# Create Sub Windows
		sub = QMdiSubWindow()
		# Do stuff in the sub windows
		sub.setWidget(QTextEdit())
		# Set The Titlebar or the Sub Window
		sub.setWindowTitle("Subby Window " + str(UI.count))
		# Add The Sub Window Into Our MDI Widget
		self.mdi.addSubWindow(sub)

		# Show the new sub window
		sub.show()

		# Position the sub windows
		# tile them
		# self.mdi.tileSubWindows()

		# Cascade them
		self.mdi.cascadeSubWindows()

		# Do more fun stuff...
		# self.mdi.closeActiveSubWindow()
		# self.mdi.removeSubWindow()
		# self.mdi.subWindowList()



# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


