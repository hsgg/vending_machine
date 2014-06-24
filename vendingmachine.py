

class VendingMachine(object):
	def __init__(self, name, price, quantity):
		self.quantity = 5
		self.price = 1.50
		self.name = 'water'

	def stock(self, name):
		return self.quantity
	def restock(self, name, quantity, price):
		self.quantity += quantity
		
	def vend(self, name, cash):
		if self.quantity == 0:
			print('none remaining')
		else:
			if cash >= self.price:		
				self.quantity -= 1
				return(cash - self.price)
			else:
				print('not enough money')
vm = VendingMachine()




'''
class drink(object):
	def __init__(self, name):
		self.quantity = 5
		self.price = 1.50
		self.name = 'water'


	def restock(self, name, quantity, price):
		self.stock += quantity


vm.restock("water", quantity=5, price=1.50)
vm.restock("iced tea", quantity=10, price=2.50)
vm.restock("soda", quantity=12, price=2.00)
'''

