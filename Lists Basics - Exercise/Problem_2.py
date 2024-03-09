# 3. Football Cards

factor = int(input())
count = int(input())

re_count = 1
my_list = []

while re_count != count + 1:
    my_list.append(factor * re_count)
    re_count += 1

print(my_list)
