from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QComboBox, QTextEdit, QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("translate.ui", self)
		self.setWindowTitle("Translator App!") 

		# Define our widgets
		self.t_button = self.findChild(QPushButton, "pushButton")
		self.c_button = self.findChild(QPushButton, "pushButton_2")

		self.combo_1 = self.findChild(QComboBox, "comboBox")
		self.combo_2 = self.findChild(QComboBox, "comboBox_2")

		self.text_1 = self.findChild(QTextEdit, "textEdit")
		self.text_2 = self.findChild(QTextEdit, "textEdit_2")

		# Click the buttons
		self.t_button.clicked.connect(self.translate)
		self.c_button.clicked.connect(self.clear)

		# Add languages to the combo boxes
		self.languages = googletrans.LANGUAGES
		#print(self.languages)

		# Convert to list
		self.language_list = list(self.languages.values())
		#print(self.language_list)

		# Add items to combo boxes
		self.combo_1.addItems(self.language_list)
		self.combo_2.addItems(self.language_list)

		# Set default combo item
		self.combo_1.setCurrentText("english")
		self.combo_2.setCurrentText("german")


		# Show The App
		self.show()

	def clear(self):
		#Clear the text boxes
		self.textEdit.setText("")
		self.textEdit_2.setText("")

		# Reset the combo boxes
		self.combo_1.setCurrentText("english")
		self.combo_2.setCurrentText("german")

	def translate(self):
		try:
			# Get Original Language Key
			for key,value in self.languages.items():
				if (value == self.combo_1.currentText()):
					from_language_key = key

			# Get translated Language Key
			for key,value in self.languages.items():
				if (value == self.combo_2.currentText()):
					to_language_key = key


			#self.text_1.setText(from_language_key)
			#self.text_2.setText(to_language_key)

			# Turn original text into a textblob
			words = textblob.TextBlob(self.text_1.toPlainText())

			# Translate words!
			words = words.translate(from_lang=from_language_key, to=to_language_key)

			# Output to text_2
			self.text_2.setText(str(words))


		except Exception as e:
			QMessageBox.about(self, "Translator", str(e))





	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

