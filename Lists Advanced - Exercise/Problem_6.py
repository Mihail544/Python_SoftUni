# 6. Electron Distribution

electrons = int(input())


def fill_shells(balance):

    return_list = []

    for n in range(1, 20):
        result = 2*(n**2)

        if result < balance:
            balance -= result
            return_list.append(result)

        if result >= balance:
            return_list.append(balance)
            return return_list


print(fill_shells(electrons))
