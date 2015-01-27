import gc
import random
from bicycles import *

#/////////////////////////////////////
#Code goes here

allcustomers = []
affordablebikes = {}


#Set bicycles, shop, customers
bikeone = Bicycle("Bikeone",10,100)
biketwo = Bicycle("Biketwo",20,200)
bikethree = Bicycle("Bikethree",30,300)
bikefour = Bicycle("Bikefour",40,400)
bikefive = Bicycle("Bikefive",50,500)
bikesix = Bicycle("Bikesix",60,600)

bikes = {bikeone:2, biketwo:4, bikethree:8, bikefour:4, bikefive:3, bikesix:5}
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


def inventory_profit():
	print bikeshop.inventory, bikeshop.profit

inventory_profit()