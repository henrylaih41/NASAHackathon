from model.modelConst import *
from model.player import *
from model.pack import *
from mapConst import *
import random
class GameModel():
	def __init__(self):
		self.player = Player()
		self.pack = Pack()
		self.site = startMap

		self.randomEven = None
		self.temperature = None
		self.height = None
		self.longitude = 0
		self.latitude = 0

	def initilize(self):
		pass

	def mapEvent(self,inputer):
		# self.site["i"]
		pass

	def update(self,inpu):
		if inpu["part"] == pack:
			self.pack.take(inpu["target"])
		else:
			print("HIHIHIHI")

