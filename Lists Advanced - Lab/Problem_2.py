# 2. Trains

wagons = int(input())
train = [0 for _ in range(wagons)]

while True:

    command = input()

    if command == "End":
        break

    else:
        command = command.split()

    if command[0] == "add":
        passengers_to_add = command[1]
        train[-1] += int(passengers_to_add)

    if command[0] == "insert":
        wagon_number = command[1]
        passengers_to_add = command[2]

        train[int(wagon_number)] += int(passengers_to_add)

    if command[0] == "leave":
        wagon_number = command[1]
        passengers_to_remove = command[2]

        train[int(wagon_number)] -= int(passengers_to_remove)

print(train)
