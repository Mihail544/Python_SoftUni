# 1. Social Distribution

population = [int(x) for x in input().split(", ")]
index_of_wealth = int(input())

total_wealth = sum(population)
required_wealth = len(population) * index_of_wealth

if total_wealth < required_wealth:
    print("No equal distribution possible")
else:
    lower_class = [p for p in population if p < index_of_wealth]
    higher_class = [p for p in population if p >= index_of_wealth]

    for person_index, person in enumerate(lower_class):
        to_take = -1
        money_cut = index_of_wealth - person

        while True:
            if higher_class[to_take] - money_cut >= index_of_wealth:
                higher_class[to_take] -= money_cut
                lower_class[person_index] += money_cut
                break
            else:
                to_take -= 1

    combined_list = lower_class + higher_class
    print(combined_list)
