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
		my_label = qtw.QLabel("Hello World! What's Your Name?")
		# Change the font size of label
		my_label.setFont(qtg.QFont('Helvetica', 18))
		self.layout().addWidget(my_label)

		# Create an entry box
		my_entry = qtw.QLineEdit()
		my_entry.setObjectName("name_field")
		my_entry.setText("")
		self.layout().addWidget(my_entry)

		# Create a button
		my_button = qtw.QPushButton("Press Me!", 
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)

		# Show the app
		self.show()

		def press_it():
			# Add name to label
			my_label.setText(f'Hello {my_entry.text()}!')
			# Clear the entry box
			my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()