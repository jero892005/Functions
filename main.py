def circle_area(r):
    pi = 3.14159
    return pi * r ** 2


def taxes(m, t):
    return m + (m * (t / 100))


def temperature(f):
    return (f - 32) * (5 / 9)


# Circle
radius_input = float(input())
circle_result = circle_area(radius_input)
print("%.2f" % circle_result)

# Taxes
money_input = float(input())
tax_input = float(input())
tax_result = taxes(money_input, tax_input)
print("%.2f" % tax_result)

# Temperature
fahrenheit_input = float(input())
temperature_result = temperature(fahrenheit_input)
print(temperature_result)