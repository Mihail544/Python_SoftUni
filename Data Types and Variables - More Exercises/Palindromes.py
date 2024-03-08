

def is_palindromes():
    word = input()
    revers = word[::-1]

    if word == revers:
        print("good")
    else:
        print("bad")


is_palindromes()
