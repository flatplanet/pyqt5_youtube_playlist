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
		my_label = qtw.QLabel("Pick Something From The List Below")
		# Change the font size of label
		my_label.setFont(qtg.QFont('Helvetica', 24))
		self.layout().addWidget(my_label)

		# Create an Combo box
		my_combo = qtw.QComboBox(self, 
			editable=True,
			insertPolicy=qtw.QComboBox.InsertAtBottom)

		# Add Items To The Combo Box
		my_combo.addItem("Pepperoni", "Something")
		my_combo.addItem("Cheese", 2)
		my_combo.addItem("Mushroom", qtw.QWidget)
		my_combo.addItem("Peppers")
		my_combo.addItems(["One", "Two", "Three"])
		my_combo.insertItems(2, ["One", "two", "Third Thing"])


		# Put combobox on the screen
		self.layout().addWidget(my_combo)

		# Create a button
		my_button = qtw.QPushButton("Press Me!", 
			clicked = lambda: press_it())
		self.layout().addWidget(my_button)

		# Show the app
		self.show()

		def press_it():
			# Add name to label
			my_label.setText(f'You Picked {my_combo.currentText()}!')
			

app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()