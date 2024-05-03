# 8. Decipher This!

message = input().split()


def decipher(word):
    count = -1
    first_leather = ""
    for symbol in word:
        if symbol.isdigit():
            count += 1
            first_leather += symbol

    first_leather = chr(int(first_leather))
    second_leather = word[-1]
    last_leather = word[count+1]
    if len(word[count:]) > 2:
        new_word = "" + first_leather + second_leather + word[count+2:-1] + last_leather
    else:
        new_word = "" + first_leather + second_leather + word[count + 2:]
    return new_word


t = ""
for word in message:
    t += decipher(word) + " "
print(t)
