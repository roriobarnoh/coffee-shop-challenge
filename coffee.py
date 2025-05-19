class Coffee:
    def __init__(self, name):
        if not (isinstance(name, str) and len(name) >= 3):
            raise Exception("Coffe name must have atleast 3 characters")
        else:
            self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        return self._orders
  
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_of_orders(self):
       len(self._orders) 

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)

    
