import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# Add a title
		self.setWindowTitle("Hello World!!")

		# Set Vertical layout
		self.setLayout(qtw.QVBoxLayout())

		# Create A Label
		my_label = qtw.QLabel("Type Something Into The Box Below", self)
		# Change the font size of label
		my_label.setFont(qtg.QFont('Helvetica', 24))
		self.layout().addWidget(my_label)

		# Create an Text box
		my_text = qtw.QTextEdit(self,
			plainText="This is real text!",
			#html = "<center><h1><em>Big Header Text!</em></h1></center>",
			acceptRichText= False,
			lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
			lineWrapColumnOrWidth=75,
			placeholderText="Hello World!",
			readOnly=True,
			)
		# Change font size of spinbox
		#my_spin.setFont(qtg.QFont('Helvetica', 18))
		

		# Put combobox on the screen
		self.layout().addWidget(my_text)

		# Create a button
		my_button = qtw.QPushButton("Press Me!", 
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)

		# Show the app
		self.show()

		def press_it():
			# Add name to label
			my_label.setText(f'You Typed {my_text.toPlainText()}!')
			my_text.setPlainText("You Pressed The Button!")

app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()