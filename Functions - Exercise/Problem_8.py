# 8. Palindrome Integers

numbers = input().split(", ") # test: 32, 2, 232, 1010


def palindrome_checker(to_check):
    for data in to_check:
        if data[:] == data[-1::-1]:
            print("True")
        else:
            print("False")


palindrome_checker(numbers)
