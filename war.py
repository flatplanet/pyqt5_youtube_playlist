from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("war.ui", self)
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
		# Keep track of scores
		self.dealer_score = 0
		self.player_score = 0


		# Grab a random Card for Dealer
		self.dealer_card = random.choice(self.deck)
		# Remove That Card From The Deck
		self.deck.remove(self.dealer_card)
		# Add That Card To Dealers List
		self.dealer.append(self.dealer_card)
		#Output Card To Screen
		pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
		self.dealerLabel.setPixmap(pixmap)

		# Grab a random Card for Player
		self.player_card = random.choice(self.deck)
		# Remove That Card From The Deck
		self.deck.remove(self.player_card)
		# Add That Card To Dealers List
		self.player.append(self.player_card)
		#Output Card To Screen
		pixmap = QPixmap(f'images/cards/{self.player_card}.png')
		self.playerLabel.setPixmap(pixmap)

		# Update Titlebar
		self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

		# Determine Score
		self.score()

	def dealCards(self):
		try:
			# Grab a random Card for Dealer
			self.dealer_card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(self.dealer_card)
			# Add That Card To Dealers List
			self.dealer.append(self.dealer_card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
			self.dealerLabel.setPixmap(pixmap)

			# Grab a random Card for Player
			self.player_card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(self.player_card)
			# Add That Card To Dealers List
			self.player.append(self.player_card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{self.player_card}.png')
			self.playerLabel.setPixmap(pixmap)

			# Update Titlebar
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

			# Determine Score
			self.score()

		except:
			# Tie
			if self.dealer_score == self.player_score:
				self.setWindowTitle(f"Game Over ||  TIE!  ||  {self.dealer_score} to {self.player_score}")
			# Dealer Wins
			elif self.dealer_score > self.player_score:
				self.setWindowTitle(f"Game Over ||  Dealer Wins!  ||  {self.dealer_score} to {self.player_score}")
			# Player Wins
			else:
				self.setWindowTitle(f"Game Over ||  Player Wins!  ||  {self.player_score} to {self.dealer_score}")	
	

	def score(self):
		# Strip out the card number
		self.dealer_card = int(self.dealer_card.split("_", 1)[0])
		self.player_card = int(self.player_card.split("_", 1)[0])

		# Compare The Card Numbers
		# Tie
		if self.dealer_card == self.player_card:
			self.dealerHeaderLabel.setText("Tie!")
			self.playerHeaderLabel.setText("Tie!")
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck    ||    Dealer: {self.dealer_score}    Player: {self.player_score}")

		# Dealer Wins
		elif self.dealer_card > self.player_card:
			self.dealerHeaderLabel.setText("Dealer Wins!")
			self.playerHeaderLabel.setText("Player Loses")
			# Update Score
			self.dealer_score += 1
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck    ||    Dealer: {self.dealer_score}    Player: {self.player_score}")

		# Player Wins
		else:
			self.dealerHeaderLabel.setText("Dealer Loses")
			self.playerHeaderLabel.setText("Player Wins!")
			# Update Score
			self.player_score += 1
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck    ||    Dealer: {self.dealer_score}    Player: {self.player_score}")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

