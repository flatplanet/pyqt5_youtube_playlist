from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("deck.ui", self)
		self.setWindowTitle("Deal Cards") 
		

		# Define our widgets
		self.dealerLabel = self.findChild(QLabel, "dealerlabel")
		self.playerLabel = self.findChild(QLabel, "playerLabel")
		self.dealerHeaderLabel = self.findChild(QLabel, "dlabel")
		self.playerHeaderLabel = self.findChild(QLabel, "plabel")

		self.shuffleButton = self.findChild(QPushButton, "spushButton")
		self.dealButton = self.findChild(QPushButton, "dpushButton")

		# Shuffle Cards
		self.shuffle()

		# Click Buttons
		self.shuffleButton.clicked.connect(self.shuffle)
		self.dealButton.clicked.connect(self.dealCards)

		# Show The App
		self.show()
		


	def shuffle(self):
		# Define Our Deck
		suits = ["diamonds", "clubs", "hearts", "spades"]
		values = range(2, 15)
		# 11 = Jack, 12=Queen, 13=King, 14=Ace

		# Create Deck
		#global deck
		self.deck = []

		for suit in suits:
			for value in values:
				self.deck.append(f"{value}_of_{suit}")
		
		# Create Our Players
		#global dealer, player
		self.dealer = []
		self.player = []

		# Grab a random Card for Dealer
		card = random.choice(self.deck)
		# Remove That Card From The Deck
		self.deck.remove(card)
		# Add That Card To Dealers List
		self.dealer.append(card)
		#Output Card To Screen
		pixmap = QPixmap(f'images/cards/{card}.png')
		self.dealerLabel.setPixmap(pixmap)

		# Grab a random Card for Player
		card = random.choice(self.deck)
		# Remove That Card From The Deck
		self.deck.remove(card)
		# Add That Card To Dealers List
		self.player.append(card)
		#Output Card To Screen
		pixmap = QPixmap(f'images/cards/{card}.png')
		self.playerLabel.setPixmap(pixmap)

		# Update Titlebar
		self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

	def dealCards(self):
		try:
			# Grab a random Card for Dealer
			card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(card)
			# Add That Card To Dealers List
			self.dealer.append(card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{card}.png')
			self.dealerLabel.setPixmap(pixmap)

			# Grab a random Card for Player
			card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(card)
			# Add That Card To Dealers List
			self.player.append(card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{card}.png')
			self.playerLabel.setPixmap(pixmap)

			# Update Titlebar
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

		except:
			self.setWindowTitle("Game Over")
			

	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

