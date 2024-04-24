# 12. Factorial Division

def factorial_division(num1, num2):
    def factorial(num):
        result = 1
        for n in range(1, num + 1):
            result *= n
        return result

    factorial_num1 = factorial(num1)

    factorial_num2 = factorial(num2)

    return factorial_num1 // factorial_num2


num1 = int(input())
num2 = int(input())

print("{:.2f}".format(factorial_division(num1, num2)))
