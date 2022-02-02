from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("blackjack.ui", self)
		self.setWindowTitle("BlackJack!") 
		

		# Define our widgets
		self.dealerCard1 = self.findChild(QLabel, "dealerCard1")
		self.dealerCard2 = self.findChild(QLabel, "dealerCard2")
		self.dealerCard3 = self.findChild(QLabel, "dealerCard3")
		self.dealerCard4 = self.findChild(QLabel, "dealerCard4")
		self.dealerCard5 = self.findChild(QLabel, "dealerCard5")
		
		self.playerCard1 = self.findChild(QLabel, "playerCard1")
		self.playerCard2 = self.findChild(QLabel, "playerCard2")
		self.playerCard3 = self.findChild(QLabel, "playerCard3")
		self.playerCard4 = self.findChild(QLabel, "playerCard4")
		self.playerCard5 = self.findChild(QLabel, "playerCard5")

		self.dealerHeaderLabel = self.findChild(QLabel, "dlabel")
		self.playerHeaderLabel = self.findChild(QLabel, "plabel")

		self.shuffleButton = self.findChild(QPushButton, "spushButton")
		self.hitMeButton = self.findChild(QPushButton, "hitMeButton")
		self.standButton = self.findChild(QPushButton, "standButton")


		# Shuffle Cards
		self.shuffle()

		# Click Buttons
		self.shuffleButton.clicked.connect(self.shuffle)
		self.hitMeButton.clicked.connect(self.playerHit)

		# Show The App
		self.show()
		


	def shuffle(self):
		# Reset Card Images
		pixmap = QPixmap('images/cards/green.png')
		self.dealerCard1.setPixmap(pixmap)
		self.dealerCard2.setPixmap(pixmap)
		self.dealerCard3.setPixmap(pixmap)
		self.dealerCard4.setPixmap(pixmap)
		self.dealerCard5.setPixmap(pixmap)
		
		self.playerCard1.setPixmap(pixmap)
		self.playerCard2.setPixmap(pixmap)
		self.playerCard3.setPixmap(pixmap)
		self.playerCard4.setPixmap(pixmap)
		self.playerCard5.setPixmap(pixmap)

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
		self.playerSpot = 0
		self.dealerSpot = 0

		self.dealerHit()
		self.dealerHit()

		self.playerHit()
		self.playerHit()
		
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
			self.dealerCard1.setPixmap(pixmap)

			# Grab a random Card for Player
			card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(card)
			# Add That Card To Dealers List
			self.player.append(card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{card}.png')
			self.playerCard1.setPixmap(pixmap)

			# Update Titlebar
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

		except:
			self.setWindowTitle("Game Over")
			
	def dealerHit(self):
		if self.dealerSpot < 5:
			try:
				# Grab a random Card for Player
				card = random.choice(self.deck)
				# Remove That Card From The Deck
				self.deck.remove(card)
				# Add That Card To Dealers List
				self.dealer.append(card)
				#Output Card To Screen
				pixmap = QPixmap(f'images/cards/{card}.png')
				
				if self.dealerSpot == 0:
					self.dealerCard1.setPixmap(pixmap)
					self.dealerSpot += 1
				
				elif self.dealerSpot == 1:
					self.dealerCard2.setPixmap(pixmap)
					self.dealerSpot += 1
				
				elif self.dealerSpot == 2:
					self.dealerCard3.setPixmap(pixmap)
					self.dealerSpot += 1

				elif self.dealerSpot == 3:
					self.dealerCard4.setPixmap(pixmap)
					self.dealerSpot += 1

				elif self.dealerSpot == 4:
					self.dealerCard5.setPixmap(pixmap)
					self.dealerSpot += 1

				# Update Titlebar
				self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

			except:
				self.setWindowTitle("Game Over")


	def playerHit(self):
		if self.playerSpot < 5:
			try:
				# Grab a random Card for Player
				card = random.choice(self.deck)
				# Remove That Card From The Deck
				self.deck.remove(card)
				# Add That Card To Dealers List
				self.player.append(card)
				#Output Card To Screen
				pixmap = QPixmap(f'images/cards/{card}.png')
				
				if self.playerSpot == 0:
					self.playerCard1.setPixmap(pixmap)
					self.playerSpot += 1
				
				elif self.playerSpot == 1:
					self.playerCard2.setPixmap(pixmap)
					self.playerSpot += 1
				
				elif self.playerSpot == 2:
					self.playerCard3.setPixmap(pixmap)
					self.playerSpot += 1

				elif self.playerSpot == 3:
					self.playerCard4.setPixmap(pixmap)
					self.playerSpot += 1

				elif self.playerSpot == 4:
					self.playerCard5.setPixmap(pixmap)
					self.playerSpot += 1

				# Update Titlebar
				self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

			except:
				self.setWindowTitle("Game Over")
	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

