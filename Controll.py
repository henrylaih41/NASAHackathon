import pygame as pg
import time
from const import *
import model.model as model
#########################
#	record game state
#	
class Controll():
	def __init__(self):
		#init view and model

		# the things show in window
		self.gameState = OPEN_PAGE

		# correspond to left side buttons for next step
		self.nextStage = []

		# 
		self.model = model