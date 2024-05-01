# 7. Group of 10's

import math


sequence_of_numbers = [int(num) for num in input().split(", ")]
max_number = max(sequence_of_numbers)

for n in range(1, (math.ceil(max_number / 10)) + 1):
    n *= 10
    turn_of_num = range(n - 9, n+1)
    print(f"Group of {n}'s: {[num for num in sequence_of_numbers if num in turn_of_num]}")
