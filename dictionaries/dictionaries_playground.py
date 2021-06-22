groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

print(groceries)
print()

# looking at a specific value
print(groceries["Baby Spinach"])
print(groceries["Crackers"])

# update item
groceries["Crackers"] = 1.5
print(groceries)

# adding a new item
groceries["Avocadoes"] = 1.00
print(groceries)

# delete item
del groceries["Bacon"]
print(groceries)

for item in groceries:
    # print(item)
    print(f"{item}: ${groceries[item]}")

for item, price in groceries.items():
    print(f"{item}: ${price}")
