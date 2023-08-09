# 8. * Party Profit

group_size = int(input())
adventure_days: int = int(input())
wallet = 0


def every_day():
    global wallet
    wallet += 50
    wallet -= group_size * 2


def every_third():
    global wallet
    wallet -= group_size * 3


def every_fifth():
    global wallet
    wallet += group_size * 20


def every_tenth():
    global group_size
    group_size -= 2


def every_fifteenth():
    global group_size
    group_size += 5


for day in range(1, adventure_days + 1):

    every_day()

    if day % 3 == 0:
        every_third()

    if day % 5 == 0:
        every_fifth()
        if day % 3 == 0:
            wallet -= group_size * 2

    if day % 15 == 0:
        every_fifteenth()

    if day % 10 == 0:
        every_tenth()

print(f"{group_size} companions received {wallet // group_size} coins each.")
