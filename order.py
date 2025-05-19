from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        self._cutomer = customer
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instace")
        self._coffee = coffee
        if not isinstance(price, float) or not(1.0 <= price <=10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")
        self._price = price
        
        self._coffee._orders.append(self)
        self._cutomer._orders.append(self)

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    @property
    def price(self):
        return self._price