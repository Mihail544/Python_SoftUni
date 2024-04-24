# 2. Add and Subtract

def add_and_subtract(number1, number2, number3):
    def sum_numbers(number1, number2):
        return number1 + number2

    def subtract(numbers_1_2, number3):
        return numbers_1_2 - number3

    numbers_1_2 = sum_numbers(number1, number2)
    print(subtract(numbers_1_2, number3))


number1 = int(input())
number2 = int(input())
number3 = int(input())

add_and_subtract(number1, number2, number3)
