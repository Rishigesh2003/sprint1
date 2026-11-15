def get_number(prompt):
        while True:
            try:
                num = int(input(prompt))
                return num
            except ValueError:
                print("Invalid, Try again!")


a = get_number("Guess the number: ")
print(a)

