from model.modelConst import *
from model.player import *
from model.pack import *
from mapConst import *
from src.predict import *
import random
import time
class GameModel():
	def __init__(self):
		self.player = Player()
		self.pack = Pack()
		self.site = startMap
		self.tp = temp_press()

		self.randomEven = None
		self.temperature = None
		self.pressure = None
		self.height = None
		self.longitude = 0
		self.latitude = 0

	def initilize(self):
		self.time = 1


	def move(self,target):
		# print("?????????????")
		self.longitude = target["site"][0]
		self.latitude = target["site"][1]
		self.tp.upgrade(self.longitude,self.latitude)
		self.tp.set_basic(self.time,self.longitude,self.latitude)
		self.temperature = self.tp.predict_temp(self.longitude,self.latitude)
		self.pressure = self.tp.predict_press(self.longitude,self.latitude)
		ev = {"temp":self.temperature,
				"pressure":self.pressure,
				"day":int(self.time),
				"hour":int(24*(self.time-int(self.time)))} 
		# print(self.player)
		pl = self.player.getState()
		return {**ev, **pl}
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

