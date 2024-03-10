# 5. Faro Shuffle

deck = input().split()
times_to_cut = int(input())


for _ in range(times_to_cut):

    deck_len = len(deck)
    Faro_deck = []

    left_deck = deck[:deck_len // 2]
    right_deck = deck[deck_len // 2:]

    for _ in range(deck_len//2):
        Faro_deck.append(left_deck[0])
        left_deck.pop(0)
        Faro_deck.append(right_deck[0])
        right_deck.pop(0)

    deck = Faro_deck


print(deck)
