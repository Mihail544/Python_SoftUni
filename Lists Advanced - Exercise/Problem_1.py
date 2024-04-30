# 1. Which Are In?


to_find = input().split(", ")
strings = input().split(", ")
answer = []

for word in to_find:
    for string in strings:
        if word in string:
            answer.append(word)
            break

print(answer)
