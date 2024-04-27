# 5. Sorting Names

names = input().split(", ")

names = [(name, len(name)) for name in names]
names.sort(key=lambda name: (-name[1], name[0]))

sorted_names = [name[0] for name in names]

print(sorted_names)