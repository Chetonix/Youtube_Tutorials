import csv

# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# print(type(item1) )
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

class Item:
    pay_rate = 0.8 #Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
    # Run validations to the recieved arguments
        assert price >= 0, f"Price:{price} is not greater than zero"
        assert quantity >= 0, f"Quantity:{quantity} is not greater than zero"

    #Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity

    # Actions to execute
        Item.all.append(self)

    @property #Property Decorator - Read Only Attribute
    def name(self):
        return self._name #a __ will compeletely shut of the accesssing of name outside of the class

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else :
            self._name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            # print(reader)
            items = list(reader)
            # print(items)
        for item in items:
             Item (
                 name = item.get('name'),
                 price = float(item.get('price')),
                 quantity = float(item.get('quantity'))
             )

    @staticmethod 
    def is_integer(num):
        if isinstance (num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    # @property
    # def read_only_name(self):
    #     return "AAA"