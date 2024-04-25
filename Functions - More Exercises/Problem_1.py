# 1. Data Types


def data_type(type_data, data):
    if type_data == "int":
        return int(data) * 2

    if type_data == "real":
        return "{:.2f}".format(float(data) * 1.5)

    if type_data == "string":
        return f"${data}$"


type_data = input()
data = input()

print(data_type(type_data, data))
