# 4. Number Classification

numbers_list = [int(num) for num in input().split(", ")]

positive_num = [str(num) for num in numbers_list if num >= 0]
negative_num = [str(num) for num in numbers_list if num < 0]
even_num = [str(num) for num in numbers_list if num % 2 == 0]
odd_num = [str(num) for num in numbers_list if num % 2 != 0]

print("Positive:", ", ".join(positive_num))
print("Negative:", ", ".join(negative_num))
print("Even:", ", ".join(even_num))
print("Odd:", ", ".join(odd_num))
