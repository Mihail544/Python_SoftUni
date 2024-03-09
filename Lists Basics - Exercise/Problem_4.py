# 4. Number Beggars

items = input().split()
items = [numbers.replace(",", "") for numbers in items]
items = [int(numbers) for numbers in items]

beggars = int(input())
stolen_goods = []

for beggar in range(beggars):
    stolen_goods.append(0)

while len(items) > 0:
    for beggar in range(beggars):
        if len(items) > 0:
            stolen_goods[beggar] += items[0]
            items.pop(0)
        else:
            break

print(stolen_goods)
