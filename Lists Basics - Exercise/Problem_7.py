# 7. * Easter Gifts

planed_gifts = ["Eggs", "StuffedAnimal", "Cozonac", "Sweets", "EasterBunny", "Eggs", "Clothes"]
commands_deck = ["OutOfStock Eggs", "Required Spoon 2", "JustInCase ChocolateEgg", "No Money"]

# while True:
#    command = input()
#    commands_deck.append(command)
#    if command != "No Money":
#        pass
#    else:
#        break

print(planed_gifts)
print(commands_deck)



for command in commands_deck:
    if command[:10] == "OutOfStock":
        gift_to_None = command[11:]

        for gift in planed_gifts:
            if gift == gift_to_None:
                planed_gifts[gift] = None

    elif command[:8] == "Required":
        print("Required")
    elif command[:10] == "JustInCase":
        print("JustInCase")
    elif command == "No Money":
        print("No Money")

print(planed_gifts)
