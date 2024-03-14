# 7. * Easter Gifts

planned_gifts = input().split()

while True:

    command_input = input()

    if command_input != "No Money":
        command = command_input.split()

        if command[0] == "OutOfStock":
            gift_name = command[1]

            for number in range(len(planned_gifts)):
                if planned_gifts[number] == gift_name:
                    planned_gifts[number] = "None"

        elif command[0] == "Required":
            new_gift_name = command[1]
            old_gift_index = int(command[2])

            if 0 <= old_gift_index < len(planned_gifts):

                planned_gifts[old_gift_index] = new_gift_name

        elif command[0] == "JustInCase":
            gift_name = command[1]
            planned_gifts[-1] = gift_name

    else:
        break


remaining_gifts = [gift for gift in planned_gifts if gift != "None"]

print(" ".join(remaining_gifts))
