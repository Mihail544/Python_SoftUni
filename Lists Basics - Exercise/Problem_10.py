# 10 * Bread Factory

max_energy = 100
energy = 100
coins = 100
day = True

day_events = input().split("|")

for event in day_events:

    event = event.split("-")

    event_name = event[0]
    event_value = int(event[1])

    if event_name == "rest":
        energy_to_refill = max_energy - energy

        if event_value < energy_to_refill:
            print(f"You gained {event_value} energy.")
            energy += event_value
        else:
            print(f"You gained {energy_to_refill} energy.")
            energy = 100
        print(f"Current energy: {energy}.")

    elif event_name == "order":

        if energy >= 30:

            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= event_value:

            coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            day = False
            break

if day:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
