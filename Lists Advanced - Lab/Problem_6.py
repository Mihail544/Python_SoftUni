# 6. Even Numbers

list_of_numbers = input().split(", ")
list_of_numbers = [int(num) for num in list_of_numbers]
list_of_index = [index for index, num in enumerate(list_of_numbers) if num % 2 == 0]

print(list_of_index)
