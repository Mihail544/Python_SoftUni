# 1. Smallest of Three Numbers

def smallest_of_the_three(*numbers):
    return min(numbers)


numbers_list = []

for _ in range(3):
    number = int(input())
    numbers_list.append(number)

print(smallest_of_the_three(*numbers_list))
