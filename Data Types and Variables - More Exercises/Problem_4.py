# 4. Balanced Brackets

# I will need to fix it :(

n = int(input())

stack = []

for _ in range(n):
    line = input()

    if line == "(":
        stack.append("(")
    elif line == ")":
        if len(stack) == 0 or stack[-1] != "(":
            print("UNBALANCED")
            break
        stack.pop()

if len(stack) == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

print("done")
