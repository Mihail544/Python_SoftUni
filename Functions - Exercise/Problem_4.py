# 4. Odd and Even Sum

digits = [int(digit) for digit in input()]


def Odd_and_Even_Sum(digits):

    even_digits = []
    odd_digits = []

    for digit in digits:
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)

    print(f"Odd sum = {sum(odd_digits)}, Even sum = {sum(even_digits)}")


Odd_and_Even_Sum(digits)
