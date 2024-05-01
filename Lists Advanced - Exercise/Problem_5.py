# 5. Office Chairs

rooms = int(input())
chairs_and_visitors = []

for _ in range(rooms):
    chairs_and_visitors.append(input())


def office_chairs(chairs_and_visitors):
    valid = True
    room = 0
    free_chairs = 0

    for data in chairs_and_visitors:

        room += 1
        chairs_number = len(data.split()[0])
        needed_chairs = int(data.split()[1])

        if chairs_number < needed_chairs:
            print(f"{(needed_chairs - chairs_number)} more chairs needed in room {room}")
            valid = False
        else:
            free_chairs += (chairs_number - needed_chairs)

    if valid:
        print(f"Game On, {free_chairs} free chairs left")


office_chairs(chairs_and_visitors)
