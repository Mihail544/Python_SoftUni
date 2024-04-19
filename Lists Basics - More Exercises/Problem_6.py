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
            if odd_or_even == "even" and even_list:

                max_even = max(even_list)
                max_even_index = list_of_numbers.index(max_even)
                print(max_even_index)

            elif odd_or_even == "odd" and odd_list:
                max_odd = max(odd_list)
                max_odd_index = list_of_numbers.index(max_odd)
                print(max_odd_index)

            else:
                print("No matches")

        elif command[0] == "min":
            if odd_or_even == "even" and even_list:

                min_even = min(even_list)
                min_even_index = list_of_numbers.index(min_even)
                print(min_even_index)

            elif odd_or_even == "odd" and odd_list:
                min_odd = min(odd_list)
                min_odd_index = list_of_numbers.index(min_odd)
                print(min_odd_index)

            else:
                print("No matches")

    elif command[0] == "first" or command[0] == "last":
        even_list = [int(number) for number in list_of_numbers if number % 2 == 0]
        odd_list = [int(number) for number in list_of_numbers if number % 2 == 1]

        count = int(command[1])
        odd_or_even = command[2]

        if count > len(list_of_numbers) and count > 0:
            print("Invalid count")
        else:

            if command[0] == "first":

                if odd_or_even == "even":
                    first_even = even_list[:count]
                    print(first_even)

                elif odd_or_even == "odd":
                    first_odd = odd_list[:count]
                    print(first_odd)

            elif command[0] == "last":

                if odd_or_even == "even":
                    last_even = even_list[-count:]
                    print(last_even)

                elif odd_or_even == "odd":
                    last_odd = odd_list[-count:]
                    print(last_odd)

print(list_of_numbers)
