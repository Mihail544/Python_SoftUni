# 5. Numbers Filter

n = int(input())

list_of_ints = []

for numbers in range(n):
    number = int(input())
    list_of_ints.append(number)

command = input()


if command == "positive":
    list_of_ints = [number for number in list_of_ints if number >= 0]
elif command == "negative":
    list_of_ints = [number for number in list_of_ints if number < 0]

if command == "even":
    list_of_ints = [number for number in list_of_ints if number % 2 == 0]
elif command == "odd":
    list_of_ints = [number for number in list_of_ints if number % 2 == 1]

print(list_of_ints)
