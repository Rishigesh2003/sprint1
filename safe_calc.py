def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid, Try again!")


x = get_number("Enter number 1: ")
y = get_number("Enter number 2: ")

print("Sum is:", x + y)
print("Difference is:", x - y)
print("Product is:", x * y)

try:
    print("Division is:", x / y)
except ZeroDivisionError:
    print("Can't be divided by 0")
