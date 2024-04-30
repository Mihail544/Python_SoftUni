# 3. Word Filter

strings = input().split(" ")
strings = [string for string in strings if len(string) % 2 == 0]
for string in strings:
    print(string)
