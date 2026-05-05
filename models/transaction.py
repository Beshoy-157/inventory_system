class Transaction:
    def __init__(self, product_name, qty, type):
        self.product_name = product_name
        self.qty = qty
        self.type = type  # "IN" or "OUT"

    def show(self):
        print(self.product_name, "|", self.qty, "|", self.type)