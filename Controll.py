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
		self.gameState = [OPEN_PAGE]

		# correspond to left side buttons for next step
		self.nextStage = []

		# map state
		self.map = HIDE
		self.showItem = []
		self.itemBuf = None

	def run(self):
		self.view.initView()
		self.model.initilize()
		while len(self.gameState) != 0:
			crt = self.view.userInput()
			print(crt)
			# key: "map" ,"page", "type"("item","move","windowControll","showDetail","choose","action"),"name"
			if crt["type"] == "item":
				action = "showDetail"
				self.itemBuf = crt["name"]
				self.view.update({"name":crt['name'],"action":action})

			elif crt["type"] == "move":
				# name: seashoreButton, investigationStationButton, plateauButton
				if crt["name"] == "seashoreButton":
					target = seashoreMap

				elif crt["name"] == "investigationStationButton":
					target = stationMap

				elif crt["name"] == "plateauButton":
					target = plateauMap

				self.model.move(target)

			elif crt["type"] == "windowControll":
				self.view.update({"name":crt["name"],"action":"windowControll"})

			elif crt["type"] == "choose":
				action = "choose"
				if crt["result"] == "yes":
					self.showItem.append(self.itemBuf)
					self.model.update({"part":"pack","action":"take","target":self.itemBuf})

				elif crt["result"] == "no":
					itemBuf = None
					pass

				else:
					print("WTF is Henry doing?")
					
				self.view.update({"name":self.showItem ,"action":action, "counter":len(self.model.pack.items),"result":crt["result"]})

			elif crt["type"] == "action":
				if "name" not in crt:
					print("WTF is Henry doing?")

				if crt["name"] == "startButton":
					self.gameState.append(MAIN_PAGE)
					self.model.initilize()
					self.view.update({"start":True})

				if crt["name"] == "thatsAll":
					self.gameState.append(STORY_PAGE)
					self.view.update({"start":True})

				if crt["name"] == "IGotIt":
					self.gameState.append(MAIN_PAGE)
					self.model.initilize()
					self.view.update({"start":True})

				else:
					self.model.update({"part":"action","action":crt["name"]})

			else:
				print("WTF is Henry doing?")






