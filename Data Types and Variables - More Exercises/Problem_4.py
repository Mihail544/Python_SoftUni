# 4. Balanced Brackets

number_fo_lines = int(input())
memory = []

first_check = False
second_check = False

for _ in range(number_fo_lines):
    strings = input()
    memory.append(strings)
    for part in memory:
        if first_check:
            if part == ")":
                second_check = True
            else:
                pass
        elif part == "(":
            first_check = True


if first_check and second_check:
    print("BALANCED")
else:
    print("UNBALANCED")
