# 04. Sum of Chars

N = int(input())

total_sum = 0

for _ in range(N):
    character = input()
    total_sum += ord(character)

print(f"The sum equals: {total_sum}")
