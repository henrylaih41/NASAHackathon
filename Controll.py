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

	def run(self):
		self.view.initView()
		self.model.initilize()
		while len(self.gameState) != 0:
			crt = self.view.uerInput()
			# key: "map" ,"page", "type"("item","move","windowControll","showDetail","choose","action"),"name","result"
			if crt["type"] == "item":
				action = "showDetail"
				name = crt["name"]
				# self.model.mapEvent({"name":name,"action":action})
				self.view.update({"name":name,"action":action})
			elif crt["type"] == "move":
				action = "move"
				self.model.move({"name":crt["name"],"action":"move"})

			elif crt["type"] == "windowControll":
				self.view.update({"name":crt["name"],"action":"windowControll"})

			elif crt["type"] == "showDetail":
				self.view.update({"name":crt["name"],"action":"showDetail"})

			elif crt["type"] == "choose":
				action = "choose"
				name = crt["name"]
				if crt["result"] == "yes":
					self.model.update({"part":pack,"action":take,"target":crt["name"]})
				elif crt["result"] == "no":
					continue
				else:
					print("WTF is Henry doing?")
					
				self.view.update({"name":name,"action":action, "counter":len(self.model.pack.items)})

			elif crt["type"] == "action":

			else:
				print("WTF is Henry doing?")
			# crt ~
			# viewT = self.model.update(crt)
			# self.view.update(viewT)
			# do something
			# pass

		# self.view.closeGame()
	def updateView(self, crt = {}):
		# self.
		pass	





