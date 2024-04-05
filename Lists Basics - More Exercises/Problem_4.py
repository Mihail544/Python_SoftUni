# 4. Josephus Permutation

soldiers = list(map(int, input().split()))
fetal_luck = int(input())

executed = []
index = 0

while len(soldiers) > 0:
    index = (index + fetal_luck - 1) % len(soldiers)
    executed.append(soldiers.pop(index))

print(executed)
