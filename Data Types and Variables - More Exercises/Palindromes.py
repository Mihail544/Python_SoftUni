# Трябва да проверя дали input е от думи които се четат еднакво от двете страни


def is_palindromes():
    word = input()
    revers = word[::-1]

    if word == revers:
        print("good")
    else:
        print("bad")


is_palindromes()
