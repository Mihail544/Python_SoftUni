# 5. Multiplication Sign

list_of_numbers = [int(input()), int(input()), int(input())]


def multiplication_sign(*numbers):

    count = 0

    for number in numbers:
        if number < 0:
            count += 1
        if number == 0:
            return "zero"

    if count % 2 == 0:
        return "positive"
    else:
        return "negative"


print(multiplication_sign(*list_of_numbers))
