from services.inventory import Inventory

class System:
    def __init__(self):
        self.inventory = Inventory()
        self.admin = None

    def add_admin(self, username, password):
        self.admin = (username, password)

    def login(self, username, password):
        return self.admin == (username, password)

    def add_stock(self, product, qty):
        self.inventory.add_product(product, qty)

    def sell_product(self, product, qty):
        self.inventory.remove_product(product, qty)