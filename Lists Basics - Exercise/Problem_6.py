# .6 Survival of the Biggest

numbers = input().split()
numbers = [int(number) for number in numbers]
n = int(input())


for _ in range(n):
    numbers.remove(min(numbers))

numbers = [str(number) for number in numbers]

print(", ".join(numbers))
