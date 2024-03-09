# 1. Invert Values

numbers = input()

my_list = numbers.split()
my_list = [int(number) for number in my_list]

for number in my_list:
    if number < 0:
        number_index = my_list.index(number)
        my_list[number_index] = abs(number)
    else:
        number_index = my_list.index(number)
        my_list[number_index] = -abs(number)

print(my_list)
