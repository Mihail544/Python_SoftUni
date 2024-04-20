# 4. Repeat String

def repeater(string_to_repeat, counter):
    for _ in range(counter):
        print(string_to_repeat, end="")


words = input()
count = int(input())

repeater(words, count)
