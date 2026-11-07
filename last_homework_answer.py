# homework: help mum fill up the shopping cart with random groceries!
# change "expression" so that shopping_cart contains 20 random items from groceries
# hint: you'll need to import random

import random

groceries = ["apple", "milk", "bread", "butter", "lettuce", "ham"]

# This loops 20 times and picks a random item for the cart each time
shopping_cart = [random.choice(groceries) for i in range(20)]

print(shopping_cart)

