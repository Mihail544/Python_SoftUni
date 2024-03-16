# 8. * Seize the Fire

fires = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells = []

# High = range(81, 125)
# Medium = range(51, 80)   Тук ми беше грешката ... range(1, 50) = 1...49
# Low = range(1, 50)

for fire in range(len(fires)):

    Type_of_fire = fires[fire].split()
    Fire_rank = Type_of_fire[0]
    Fire_level = int(Type_of_fire[2])
    valid = False

    if Fire_rank == "High" and 81 <= Fire_level <= 125:
        if water >= Fire_level:
            valid = True

    elif Fire_rank == "Medium" and 51 <= Fire_level <= 80:
        if water >= Fire_level:
            valid = True

    elif Fire_rank == "Low" and 1 <= Fire_level <= 50:
        if water >= Fire_level:
            valid = True

    if valid:
        water -= Fire_level
        cells.append(Fire_level)
        effort += Fire_level * 0.25
        total_fire += Fire_level


print("Cells:")
for cell in cells:
    print(f" - {cell}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
