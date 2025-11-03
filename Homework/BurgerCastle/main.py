validOrders = ('burger','fried','salad','soda','milkshake')
itemDescriptions = ( "Half-pound burger","Large fries","Side salad", "Diet root beer", "Chocolate shake")
order = []
print("Welcome to Burger Castle")
print("Menu:  ",validOrders)
print("Please enter each item in your order.  Press 'Enter' or type 'quit' on an empty line when done")
ordering = True
while ordering:
    item = input("Enter Item: ")
    if item.lower() in validOrders:
        order.append(item)
    elif item.lower() == 'quit':
        ordering = False
        break
    elif item.lower() == '':
        ordering = False
        break
    else:
        print("Sorry we don't sell "+item)
if len(order) > 0:
    print("Order complete; you are having")
    for x in order:
        index = validOrders.index(x)
        print(itemDescriptions[index])
print("Thanks for visiting Burger Castle!")