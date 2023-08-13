# 4. Balanced Brackets

def is_balanced(expression):
    stack = []
    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack

n = int(input())

for _ in range(n):
    line = input().strip()
    if is_balanced(line):
        print("BALANCED")
    else:
        print("UNBALANCED")
