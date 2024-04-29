# 7. The Office

employees_happiness = input().split(" ")
happiness_improvement = float(input())

employees_happiness = [float(employee) for employee in employees_happiness]
employees_happiness = [(employee * happiness_improvement) for employee in employees_happiness]
average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_personal = 0

for employee_happy_factor in employees_happiness:
    if employee_happy_factor >= average_happiness:
        happy_personal += 1
    else:
        pass

if happy_personal >= (len(employees_happiness) // 2):
    print(f"Score: {happy_personal}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_personal}/{len(employees_happiness)}. Employees are not happy!")
