# 9. Anonymous Threat

def merge(data, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(data):
        end_index = len(data) - 1

    merged_string = ''.join(data[start_index:end_index + 1])
    data = data[:start_index] + [merged_string] + data[end_index + 1:]
    return data


def divide(data, index, partitions):
    string_to_divide = data[index]
    length = len(string_to_divide)
    chunk_size = length // partitions
    chunks = []

    for i in range(0, length, chunk_size):
        chunks.append(string_to_divide[i:i + chunk_size])

    if sum(len(chunk) for chunk in chunks) < length:
        last_chunk = chunks.pop()
        chunks.append(last_chunk + string_to_divide[len(''.join(chunks))::])

    data = data[:index] + chunks + data[index + 1:]
    return data


data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    action, *args = command.split()

    if action == "merge":
        start_index, end_index = map(int, args)
        data = merge(data, start_index, end_index)
    elif action == "divide":
        index, partitions = map(int, args)
        data = divide(data, index, partitions)

print(' '.join(data))
