# 4. Palindrome Strings

words = input().split(" ")
palindrome = input()
palindrome_list = []

for word in words:
    if word == word[-1::-1]:
        palindrome_list.append(word)

print(f"{palindrome_list}\nFound palindrome {palindrome_list.count(palindrome)} times")
