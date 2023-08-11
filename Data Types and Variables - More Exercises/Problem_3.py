# 3. Decrypting Messages

key = int(input())
n = int(input())

list_of_crypt = []
decrypted = []
answer = []

for _ in range(n):
    crypt = input()
    list_of_crypt.append(crypt)

for crypted in list_of_crypt:
    decrypted.append(ord(crypted)+key)

new_list_of_crypt = decrypted

for numbers in new_list_of_crypt:
    answer.append(chr(numbers))


Final_answer = "".join(answer)
print(Final_answer)
