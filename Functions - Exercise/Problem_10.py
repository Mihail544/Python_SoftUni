# 10. Perfect Number

def perfect_number(number):
    can_divide = []

    for divider in range(1, number):

        if number % divider == 0:
            can_divide.append(divider)
        else:
            pass

    if sum(can_divide) == number:
        print("We have a perfect number!")
    else:
        print(" It's not so perfect.")


number = int(input())

perfect_number(number)
