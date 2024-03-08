# 4. Search

n = int(input())
word_to_check = input()

list_of_strings = []

for _ in range(n):
    word = input()
    list_of_strings.append(word)

print(list_of_strings)

list_of_strings = [correct_words for correct_words in list_of_strings if word_to_check in list_of_strings]
print(list_of_strings)
