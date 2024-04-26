# 4. Tribonacci Sequence

n = int(input())


def tribonacci_calculator(times_to_count):

    return_list = [1, 1, 2]
    time_list = [1, 1, 2]

    if times_to_count > 3:
        for _ in range(3, times_to_count):

            next_number = sum(time_list)
            return_list.append(next_number)
            time_list.append(next_number)
            time_list.pop(0)
    else:
        return return_list[:times_to_count]

    return return_list


list_of_tribonacci = tribonacci_calculator(n)
print(*list_of_tribonacci)
