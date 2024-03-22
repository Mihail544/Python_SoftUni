# 2. Messaging

numbers = input().split(" ")
text = list(input())

numbers = [sum(int(digit) for digit in number) for number in numbers]
message = []

for index in numbers:
    if len(text) > index:
        message.append(text[index])
        text.pop(index)
    else:
        message.append(text[index % len(text)])
        text.pop(index % len(text))

print("".join(message))
