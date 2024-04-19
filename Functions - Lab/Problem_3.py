# 3. Calculations

operator = input()
number1 = int(input())
number2 = int(input())


def calculation(operator, number1, number2):

    if operator == "multiply":
        return int(number1 * number2)
    if operator == "divide":
        return int(number1 / number2)
    if operator == "add":
        return int(number1 + number2)
    if operator == "subtract":
        return int(number1 - number2)


print(calculation(operator, number1, number2))
