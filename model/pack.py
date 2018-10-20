from model.modelConst import *
from itemConst import *
class Pack():
	def __init__(self):
		self.items = []
		self.open = False

	def take(self,itemNum):
		if len(self.items) == 5:
			return False
		else:
			self.items.append(itemNum)
			return True

	def check(self,item):
		return item in self.items

	def getPack(self):
		return self.items

	def abandon(self,item):
		if item not in self.items:
			return False
		self.items.remove(item)
		return True