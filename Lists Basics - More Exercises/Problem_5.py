# 5 Tic-Tac-Toe

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

count = 0
turns = []

for _ in range(3):
    number = input().split()
    for n in number:
        turns.append(int(n))

turns = [int(turn) for turn in turns]

for turn in turns:

    if turn == 0:
        pass
    elif turn == 1:
        board[count] = "x"

    elif turn == 2:
        board[count] = "o"

    count += 1

for i in range(0, 9, 3):
    print(" | ".join(board[i:i+3]))
    if i < 6:
        print("-" * 9)

first_player_win = any(all(board[i] == "x" for i in combination) for combination in winning_combinations)
second_player_win = any(all(board[i] == "o" for i in combination) for combination in winning_combinations)

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
else:
    print("Draw!")
