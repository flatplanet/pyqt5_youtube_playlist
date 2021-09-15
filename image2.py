from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("image2.ui", self)

		# Define our widgets
		self.button = self.findChild(QPushButton, "pushButton")
		self.label = self.findChild(QLabel, "label")


		# Click The Dropdown Box
		self.button.clicked.connect(self.clicker)

				
		# Show The App
		self.show()

	def clicker(self):
		#self.label.setText("You Clicked The Button!")	
		# Open File Dialog
		fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\gui\\images", "All Files (*);;Python Files (*.py);; PNG Files (*.png)" )
		
		# Output filename to screen
		if fname:
			self.pixmap = QPixmap(fname[0])
			self.label.setPixmap(self.pixmap)

			#self.label.resize(self.pixmap.width(),
            #              self.pixmap.height())
			#self.label.setText(fname[0])


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

