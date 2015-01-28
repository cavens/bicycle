import gc
import random

#/////////////////////////////////////
#Classes go here


class Wheels(object):
	"""This class does this"""
	def __init__(self,name,weight,cost):
		self.name = name
		self.weight = weight
		self.cost = cost

class Frames(object):
	"""This class does this"""
	def __init__(self,material,weight,cost):
		self.material = material
		self.weight = weight
		self.cost = cost
		materials = ["aluminum","carbon","steel"]

		if material.lower() not in materials:
			print "Frame material doesn't exist"

class Bicycle(object):
	"""This class does this"""
	def __init__(self,name,wheels,frame,manufacturer):
		self.name = name
		self.wheels = wheels
		self.frame = frame
		self.manufacturer = manufacturer

		self.cost = self.frame.cost + (2*self.wheels.cost)
		self.weight = self.frame.weight + (2*self.wheels.weight)

class Manufacturer(object):
	"""This class does this"""
	def __init__(self,name,margin):
		global wheels
		global frames
		self.name = name
		self.margin = margin

		self.modelone = Bicycle("%s %s" %(self.name, "Modelone"), random.choice(wheels), random.choice(frames), self.name)
		self.modeltwo = Bicycle("%s %s" %(self.name, "Modeltwo"), random.choice(wheels), random.choice(frames), self.name)
		self.modelthree = Bicycle("%s %s" %(self.name, "Modelthree"), random.choice(wheels), random.choice(frames), self.name)

		self.inventory = {}

		self.models = [self.modelone, self.modeltwo, self.modelthree]
		for model in self.models:
			self.inventory[model] = model.cost*self.margin

class BikeShops(object):
	"""This class does this"""
	manufacturer_inventory = {}
	for obj in gc.get_objects():
			if isinstance(obj, Manufacturer):
				manufacturer_inventory += dict(obj.inventory.items())

	def __init__(self,name,bikes,margin):
		self.name = name
		self.margin = margin
		self.price = 0 #Can be discarted?
		self.inventory = {}
		self.profit = 0

		for bike in bikes:
			price = manufacturer_inventory[bike]*self.margin
			self.inventory[bike]={"price": price, "amount": bikes[bike]}

	def sell(self,bike,customer):
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







































