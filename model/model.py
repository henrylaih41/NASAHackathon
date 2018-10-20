from model.modelConst import *
from model.player import *
from model.pack import *
from mapConst import *
import random
import time
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
		if "part" not in inpu:
			print("WTF am I doing at model.py??????")
			time.sleep(1000000000000)
			return
			
		if inpu["part"] == "pack":
			if self.pack.take(inpu["target"]):
				if self.pack.full():
					return {"action":"endChoose"}
				else:
					return {"action":None}
		else:
			print("HIHIHIHI")

