from item import Item
from phone import Phone

# phone1 = Phone("jscPhonev10", 500, 5, 1)
# item1 = Item("Phone", 100, 5)
# print(phone1.all)
# phone1.broken_phones = 1
# phone2 = Phone("jscPhonev20", 700, 5, 1)
# print(phone2.all)
# phone2.broken_phones = 1

# print(Item.all)
# print(Phone.all)

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item('MyItem', 750)

print(Item.all)
item1.name = "OtherItemmmmmmmmm"
print(Item.all)

# print(phone1.calculate_total_price())

#item1 = Item("Phone", 100, 5)
#print(type(item1.name))
# #item1.name = "Phone"
# #item1.price = 100
# item1. quantity = 5
#print(item1.calculate_total_price(item1.price, item1.quantity))

#item2 = Item("Laptop", 1000, 3)
# #item2.name = "Laptop"
# #item2.price = 1000
# item2. quantity = 3
#print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

#print(Item.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance)

# print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(12.1))