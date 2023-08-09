# 7. Water Overflow


number_of_pipes = int(input())
capacity = 255
liters_poured = 0

for _ in range(number_of_pipes):
    liters = int(input())
    if liters < capacity and liters_poured + liters <= capacity:
        liters_poured += liters

    else:
        print("Insufficient capacity!")

print(liters_poured)
