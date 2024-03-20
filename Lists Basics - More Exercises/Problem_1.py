# 1. Zeros to Back

numbers = input().split(", ")

count = 0
for number in numbers:
    if number == "0":
        count += 1

numbers = [number for number in numbers if number != "0"]

for n in range(count):
    numbers.append("0")

numbers = [int(number) for number in numbers]

print(numbers)
