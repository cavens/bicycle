import gc
import random
from bicycles import *

#/////////////////////////////////////
#Code goes here

allcustomers = []
affordablebikes = {}


#Set bicycles, shop, customers, wheels, frames
wheelone = Wheels("Wheelone",10,10)
wheeltwo = Wheels("Wheeltwo",20,20)
wheelthree = Wheels("Wheelthree",30,30)
wheels = [wheelone, wheeltwo, wheelthree]

framealu = Frames("Aluminum",10,10)
framecar = Frames("Carbon",20,20)
framesteel = Frames("Steel",30,30)
frames = [framealu, framecar, framesteel]

manufacturerone = Manufacturer("Manufacturerone",1.20)
manufacturertwo = Manufacturer("Manufacturertwo",1.20)

bikes = {manufacturerone.modelone:2, manufacturerone.modeltwo:4, manufacturerone.modelthree:8, manufacturertwo.modelone:4, manufacturertwo.modeltwo:3, manufacturertwo.modelthree:5}
bikeshop = BikeShops("Bikeshop",bikes,1.20)

customerone = Customers("Customerone",200)
customertwo = Customers("Customertwo",500)
customerthree = Customers("Customerthree",1000)


#Get all customers + bikes they can afford
def find_customers_bikes():
	"""This function does this"""
	for obj in gc.get_objects():
		if isinstance(obj, Customers):
			allcustomers.append(obj)	

	for customer in allcustomers:
		affordablebikes[customer.name] = []
		for bike in bikeshop.inventory:
			if customer.fund >= bikeshop.inventory[bike]["price"]:
				affordablebikes[customer.name].append(bike)
	print "The affordabel bikes are %s" % affordablebikes

find_customers_bikes()


#Print bikeshop inventory
def print_inventory():
	"""This function does this"""
	print bikeshop.inventory

print_inventory()


#Purchase bike, print name and cost of bike and amount of money left in fund
def purchase_bikes():
	"""This function does this"""
	#bikeshop.sell(bikeone, customerone)
	for customer in allcustomers:
		randombike = random.choice(affordablebikes[customer.name])
		bikeshop.sell(randombike, customer)
		print randombike, bikeshop.inventory[randombike]["price"], customer.fund

purchase_bikes()


#Print inventory and total profit
def inventory_profit():
	"""This function does this"""
	print bikeshop.inventory, bikeshop.profit

inventory_profit()








