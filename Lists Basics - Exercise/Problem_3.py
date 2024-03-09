# 3. Football Cards

Team_A = 11
Team_B = 11

deck = input().split()
deck = set(deck)

for card in deck:
    if Team_A > 6 and Team_B > 6:
        pass
    else:
        break
    if card[0] == "A":
        Team_A -= 1
    else:
        Team_B -= 1

print(f"Team A - {Team_A}; Team B - {Team_B}")

if Team_A < 7 or Team_B < 7:
    print("Game was terminated")
