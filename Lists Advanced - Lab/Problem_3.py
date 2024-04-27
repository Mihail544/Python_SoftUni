# 3. To-do List

to_do_list = []
return_list = []

while True:
    command = input()

    if command == "End":
        break
    else:
        to_do_list.append(command)

for n in range(11):
    for task in to_do_list:
        tasks_order = (task.split("-")[0])

        if int(tasks_order) == n:
            return_list.append(task.split("-")[1])

print(return_list)
