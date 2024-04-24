# 7. Min Max and Sum

numbers = input().split(" ")
numbers = [int(number) for number in numbers]


def min_max_sum(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)

    print(f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}")


min_max_sum(numbers)
