# 2. Next Version

current_version = input().split(".")
version = int("".join(current_version)) + 1
print(f"{str(version)[0]}.{str(version)[1]}.{str(version)[2]}")
