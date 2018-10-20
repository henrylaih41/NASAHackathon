from model.modelConst import *
class Pack():
	def __init__(self):
		self.items = []
		self.open = False

	def take(self,itemName):
		if len(self.items) == 5:
			return False
		else:
			self.items.append(itemName)
			return True

	def check(self,item):
		return item in self.items

	def full(self):
		return len(self.items) == 5

	def getPack(self):
		return self.items

	def abandon(self,item):
		if item not in self.items:
			return False
		self.items.remove(item)
		return True