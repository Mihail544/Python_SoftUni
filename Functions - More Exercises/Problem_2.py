# 2. Center Point

import math

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())


def closest_to_the_center(x1, y1, x2, y2):

    distance_1 = x1 ** 2 + y1 ** 2
    distance_2 = x2 ** 2 + y2 ** 2

    if distance_1 <= distance_2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


closest_to_the_center(x1, y1, x2, y2)
