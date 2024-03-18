items = input().split("|")
budget = float(input())
items_bag = []

for item_data in items:

    valid = False
    item_data = item_data.split("->")
    item_name = item_data[0]
    item_price = float(item_data[1])

    if item_name == "Clothes" and budget >= item_price <= 50.00:
        valid = True

    elif item_name == "Shoes" and budget >= item_price <= 35.00:
        valid = True

    elif item_name == "Accessories" and budget >= item_price <= 20.50:
        valid = True

    if valid:
        budget -= item_price
        items_bag.append(item_price)

items_with_profit = [round(item * 1.4, 2) for item in items_bag]

for item in items_with_profit:
    print(f"{item:.2f}", end=' ')

    # end=' '  Демек за всеки item вместо да се принтира на нов ред да се принтира с малко място ...

print()
print(f"Profit: {sum(items_with_profit) - sum(items_bag):.2f}")

if sum(items_with_profit) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
