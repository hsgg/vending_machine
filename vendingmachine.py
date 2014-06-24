vm = VendingMachine()

class drink(object):
	def __init__(self):
		self.stock = 5
		self.price = 1.50

vm.restock("water", quantity=5, price=1.50)
vm.restock("iced tea", quantity=10, price=2.50)
vm.restock("soda", quantity=12, price=2.00)


