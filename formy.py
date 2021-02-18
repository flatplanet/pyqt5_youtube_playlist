import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# Add a title
		self.setWindowTitle("Hello World!!")

		# Set Vertical layout
		#self.setLayout(qtw.QVBoxLayout())
		form_layout = qtw.QFormLayout()
		self.setLayout(form_layout)

		# Add Stuff/Widgets
		label_1 = qtw.QLabel("This is a Cool Label Row")
		label_1.setFont(qtg.QFont("Helvetica", 24))
		f_name = qtw.QLineEdit(self)
		l_name = qtw.QLineEdit(self)

		# Add Rows To App
		form_layout.addRow(label_1)
		form_layout.addRow("First Name", f_name)
		form_layout.addRow("Last Name", l_name)
		form_layout.addRow(qtw.QPushButton("Press Me!",
			clicked = lambda: press_it()))



		# Show the app
		self.show()
		
		def press_it():
			label_1.setText(f'You Clicked The Button, {f_name.text()} {l_name.text()}!')
		
app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()