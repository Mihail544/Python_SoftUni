# 7. Water Overflow

capacity = 225
liters_poured = 0

n = int(input())

for _ in range(n):
    liters = int(input())

    if capacity - liters >= 0:
        capacity += - liters
        liters_poured += liters
    else:
        print("Insufficient capacity!")

print(liters_poured)
