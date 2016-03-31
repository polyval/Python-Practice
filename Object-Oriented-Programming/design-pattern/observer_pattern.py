# -*- coding: utf-8 -*-

"""
	The observer pattern is useful for state monitoring
	and event handling situations. This pattern allows
	a given object to be monitored by an unknown and dynamic
	group of "observer" objects. It is mainly used to implement
	event handling systems, also it is a key part in the
	MVC architectural pattern.

	Below is an example that observer pattern using in a
	backup system. We write a core object that maintains
	certain values, and then have one or more observers
	create serialized copies of that object. These copies
	might be stored in a database, on a remote host, or in 
	a local file
"""

class Inventory:

	def __init__(self):
		self.observers = []
		self._product = None
		self._quantity = 0

	def attach(self, observer):
		self.observers.append(observer)

	@property
	def product(self):
	    return self._product
	@product.setter
	def product(self, value):
	    self._product = value
	    self._update_observers()

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
		for observer in self.observers:
			observer()


class ConsoleObserver:

	def __init__(self, inventory):
		self.inventory = inventory

	def __call__(self):
		print self.inventory.product
		print self.inventory.quantity
    

# i = Inventory()
# c = ConsoleObserver(i)
# i.attach(c)
# i.product = "widget"
# widget
# 0
# i.quantity = 5
# widget
# 5