# 5. Orders.

def order_price(product, product_quantity):
    menu = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }

    product_price = menu[product]
    total_price = product_quantity * product_price
    return total_price


product_name = input()
quantity = int(input())

print('{:.2f}'.format(order_price(product_name, quantity)))
