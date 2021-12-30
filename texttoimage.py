from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image, ImageFont, ImageDraw


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("texttoimage.ui", self)
		self.setWindowTitle("Add Text To Images!") 

		# Define our widgets
		self.label = self.findChild(QLabel, "label")
		self.edit = self.findChild(QLineEdit, "lineEdit")
		self.button = self.findChild(QPushButton, "pushButton")

		# Click the buttons
		self.button.clicked.connect(self.addText)
		
		# Show The App
		self.show()

	def addText(self):
		# Grab the text
		myText = self.edit.text()

		# Open the Image
		myImage = Image.open("images/aspen.png")

		# Define the font
		textFont = ImageFont.truetype("arial.ttf", 46)

		#Edit The Image
		editImage = ImageDraw.Draw(myImage)
		editImage.text((128, 320), myText, ("white"), font=textFont)

		# Save The Image
		myImage.save("images/aspen2.png")

		# Update our App Image
		pixmap = QPixmap("images/aspen2.png")
		self.label.setPixmap(pixmap)

		# Clear The Text Box
		self.edit.setText("")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

