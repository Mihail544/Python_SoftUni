# 1. Invert Values

numbers = input()

my_list = numbers.split()
my_list = [int(number) for number in my_list]

for index, key in enumerate(my_list):
    if key < 0:
        my_list[index] = abs(key)
    else:
        my_list[index] = -abs(key)

print(my_list)