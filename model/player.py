from model.modelConst import *

class Player():
	def __init__(self):
		self.hunger = HUGER_START
		self.spirit = SPIRIT_START 
		self.point = POINT_START
		self.thirst = 0
		# search history
		# self.

	def updateHunger(self,num):
		self.hunger += num

	def updatePoint(self,num):
		self.point += num

	def updateSpirit(self,num):
		self.spirit += num
