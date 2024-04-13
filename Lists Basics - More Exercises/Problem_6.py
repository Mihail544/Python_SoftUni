# 6. List Manipulator

list_of_numbers = input().split(" ")
list_of_numbers = [int(numbers) for numbers in list_of_numbers]

while True:
    command = input().split(" ")

    if command[0] == "end":
        break

    elif command[0] == "exchange":
        exchange_index = int(command[1])

        if exchange_index < 0 or exchange_index >= len(list_of_numbers):
            print("Invalid index")

        else:
            to_move = list_of_numbers[exchange_index + 1::]
            list_of_numbers = to_move + [number for number in list_of_numbers if number not in to_move]

    elif command[0] == "max" or command[0] == "min":
        odd_or_even = command[1]

        even_list = [int(number) for number in list_of_numbers if number % 2 == 0]
        odd_list = [int(number) for number in list_of_numbers if number % 2 == 1]

        if command[0] == "max":

            if odd_or_even == "even":
                try:
                    max_index = even_list.index(max(even_list))
                    print(max_index)
                except ValueError:
                    print("No matches")

            elif odd_or_even == "odd":
                try:
                    max_index = odd_list.index(max(odd_list))
                    print(max_index)
                except ValueError:
                    print("No matches")

        elif command[0] == "min":

            if odd_or_even == "even":
                try:
                    min_index = even_list.index(min(even_list))
                    print(min_index)
                except ValueError:
                    print("No matches")

            elif odd_or_even == "odd":
                try:
                    min_index = odd_list.index(min(odd_list))
                    print(min_index)
                except ValueError:
                    print("No matches")

    elif command[0] == "first" or command[0] == "last":
        count = int(command[1])
        odd_or_even = command[2]

        even_list = [int(number) for number in list_of_numbers if number % 2 == 0]
        odd_list = [int(number) for number in list_of_numbers if number % 2 == 1]

        if command[0] == "first":

            if odd_or_even == "even":
                if count >= len(even_list):
                    first_even = even_list[:count]
                    print(first_even)
                else:
                    print("Invalid count")

            elif odd_or_even == "odd":
                if count >= len(odd_list):
                    first_odd = odd_list[:count]
                    print(first_odd)
                else:
                    print("Invalid count")

        elif command[0] == "last":

            if odd_or_even == "even":
                if count >= len(even_list):
                    last_even = even_list[-count:]
                    print(last_even)
                else:
                    print("Invalid count")

            elif odd_or_even == "odd":
                if count >= len(odd_list):
                    last_odd = odd_list[-count:]
                    print(last_odd)
                else:
                    print("Invalid count")


print(list_of_numbers)
