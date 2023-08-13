# 4. Balanced Brackets

number_fo_lines = int(input())
balance = 0

for _ in range(number_fo_lines):
    word = input()
    for words in word:
        if words == "(":
            balance +=1
        elif words == ")":
            balance -= 1

if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
