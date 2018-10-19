import pygame as pg
import time
from const import *
from View.View import View
from model.model import GameModel

#########################
#	record game state
#	
class Controll():
	def __init__(self):
		#init view and model
		self.model = GameModel()
		self.view = View()

		# the things show in window
		self.gameState = OPEN_PAGE

		# correspond to left side buttons for next step
		self.nextStage = []

		# map state
		self.map = HIDE

	def updateView(self, crt = {}):
		# self.
		pass	

