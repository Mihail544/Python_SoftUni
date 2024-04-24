# 3. Characters in Range

def main(start_point, end_point):
    ascii_start_code = ord(start_point) + 1
    ascii_end_code = ord(end_point)
    list_of_answers = []

    for i in range(ascii_start_code, ascii_end_code):
        list_of_answers.append(chr(i))
    return list_of_answers


start_char = input()
end_char = input()

print(" ".join(main(start_char, end_char)))
