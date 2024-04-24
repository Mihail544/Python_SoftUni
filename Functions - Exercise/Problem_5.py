# 5. Even Numbers

numbers = input().split(" ")
numbers = [int(number) for number in numbers]


def is_even(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))
