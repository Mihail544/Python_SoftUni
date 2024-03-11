numbers = input().split()
numbers = [int(number) for number in numbers]

cuts = int(input())

for _ in range(cuts):
    lower = min(numbers)
    numbers.remove(lower)

numbers = [str(number) for number in numbers]

print(", ".join(numbers))

