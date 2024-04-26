# 3. Longer Line

import math

point_1 = [float(input()), float(input())]
point_2 = [float(input()), float(input())]
point_3 = [float(input()), float(input())]
point_4 = [float(input()), float(input())]


def longer_Line(point_1, point_2, point_3, point_4):

    list_of_points = [point_1, point_2, point_3, point_4]

    def distance(point):
        point_distance = [abs(cord) for cord in point]
        point_distance = sum(point_distance)
        return point_distance

    point_1_distance = distance(point_1)
    point_2_distance = distance(point_2)
    point_3_distance = distance(point_3)
    point_4_distance = distance(point_4)

    line_one = (point_1_distance + point_2_distance)
    line_two = (point_3_distance + point_4_distance)

    point_1 = [math.floor(cord) for cord in point_1]
    point_2 = [math.floor(cord) for cord in point_2]
    point_3 = [math.floor(cord) for cord in point_3]
    point_4 = [math.floor(cord) for cord in point_4]

    if line_one > line_two:
        if point_1_distance > point_2_distance:
            print(f"({point_2[0]}, {point_2[1]})({point_1[0]}, {point_1[1]})")
        else:
            print(f"({point_1[0]}, {point_1[1]})({point_2[0]}, {point_2[1]})")
    else:
        if point_3_distance > point_4_distance:
            print(f"({point_4[0]}, {point_4[1]})({point_3[0]}, {point_3[1]})")
        else:
            print(f"({point_3[0]}, {point_3[1]})({point_4[0]}, {point_4[1]})")


longer_Line(point_1, point_2, point_3, point_4)
