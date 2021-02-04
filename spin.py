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
		my_label = qtw.QLabel("Pick Something From The List Below", self)
		# Change the font size of label
		my_label.setFont(qtg.QFont('Helvetica', 24))
		self.layout().addWidget(my_label)

		# Create an Spin box
		my_spin = qtw.QSpinBox(self,
			value=10,
			maximum=100,
			minimum=0,
			singleStep=5,
			prefix="#",
			suffix="!!!",
			)
		# Change font size of spinbox
		my_spin.setFont(qtg.QFont('Helvetica', 18))
		

		# Put combobox on the screen
		self.layout().addWidget(my_spin)

		# Create a button
		my_button = qtw.QPushButton("Press Me!", 
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)

		# Show the app
		self.show()

		def press_it():
			# Add name to label
			my_label.setText(f'You Picked {my_spin.value()}!')
			

app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()