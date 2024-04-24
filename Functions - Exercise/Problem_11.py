# 11. * Loading Bar


def loading(percentage):
    board = list("[..........]")

    for dots in range(percentage // 10):
        board[dots + 1] = "%"
    if percentage != 100:

        print(f"{percentage}%", end=" ")
        print("".join(board))
        print("Still loading...")
    else:
        print(f"100% Complete!")
        print("".join(board))


num = int(input())

loading(num)
