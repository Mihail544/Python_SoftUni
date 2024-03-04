# 4. Balanced Brackets

n = int(input())

Balance = True
my_box = []
my_check_box = []

for symbols in range(n):
    symbol = input()
    if symbol == "(" or symbol == ")":
        my_box.append(symbol)


def main(brackets):
    for bracket in brackets:

        if len(my_check_box) == 0 and bracket == "(":
            my_check_box.append(bracket)
            continue
        elif len(my_check_box) == 0 and bracket == ")":
            return False

        if bracket == "(" and len(my_check_box) != 0:
            if my_check_box[-1] == ")":
                my_check_box.append(bracket)
                continue
            else:
                return False

        if bracket == ")" and len(my_check_box) != 0:
            if my_check_box[-1] == "(":
                my_check_box.append(bracket)
                continue
            else:
                return False
    return True


if main(my_box):
    print("BALANCED")
else:
    print("UNBALANCED")
