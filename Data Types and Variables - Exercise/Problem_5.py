# 5. Print Part of the ASCII Table

start = int(input())
stop = int(input())
answer = []

if start == stop:
    answer.append(chr(start))
    print(answer)
else:
    while start != stop+1:
        answer.append(chr(start))
        start += 1
    print(" ".join(answer))
