# 9. * Hello, France

items = input().split("|")
budget = float(input())
start_budget = budget
my_bag_of_items = []

for item_data in items:
    valid = False

    item_data = item_data.split("->")
    item_name = item_data[0]
    item_price = float(item_data[1])

    if item_name == "Clothes" and budget >= item_price <= 50:
        valid = True

    elif item_name == "Shoes" and budget >= item_price <= 35:
        valid = True

    elif item_name == "Accessories" and budget >= item_price <= 20.50:
        valid = True

    if valid:
        budget -= item_price
        my_bag_of_items.append(item_price)

new_item_price = [item * 1.4 for item in my_bag_of_items]

for item_price in new_item_price:

    print(f"{item_price:.2f}", end=" ")
    budget += item_price

print()
print(f"Profit: {abs(budget - start_budget):.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
