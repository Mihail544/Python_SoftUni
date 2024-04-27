# 1. No Vowels

word = input()


def remove_vowels(word):

    vowels_list = ['a', 'o', 'u', 'e', 'i']

    word = [symbol for symbol in word if symbol.lower() not in vowels_list]
    return word


print("".join(remove_vowels(word)))
