#/////////////////////////////////////
#Classes go here


class Bicycle(object):
	"""This class does this"""
	def __init__(self,name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost


class BikeShops(object):
	"""This class does this"""
	def __init__(self, name, bikes, margin):
		self.name = name
		self.margin = margin
		self.price = 0 #Can be discarted?
		self.inventory = {}
		self.profit = 0

		for bike in bikes:
			price = bike.cost * self.margin
			self.inventory[bike.name]={"price": price, "amount": bikes[bike]}

	def sell (self, bike, customer):
		self.profit += int(self.inventory[bike]["price"]-(self.inventory[bike]["price"]/self.margin))
		customer.bikesowned.append(bike)
		customer.fund -= self.inventory[bike]["price"]
		self.inventory[bike]["amount"] -= 1


class Customers(object):
	"""This class does this"""	
	bikesowned = []
	def __init__(self,name,fund):
		self.name = name
		self.fund = fund







































