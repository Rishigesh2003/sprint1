def miles_to_km(value):
    ans = value * 1.60934
    return round(ans, 2)


def km_to_miles(value):
    ans = value * 0.621371
    return round(ans, 2)


def f_to_c(value):
    ans = (value - 32) * 5 / 9
    return round(ans, 2)


def c_to_f(value):
    ans = (value * 9) / 5 + 32
    return round(ans, 2)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Wrong value, try again!")

def get_choice():
    while True:
        try:
            choice = int(input("Choose your option: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Wrong Number")
        except ValueError:
            print("Invalid, Try again")

def show_menu():
    print("=== Unit Converter ===")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Quit")

def main():

    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            miles = get_float("Enter the value in Miles: ")
            print("The Converted Km is:" , miles_to_km(miles), "Km")

        elif choice == 2:
            km = get_float("Enter the value in KM: ")
            print("The Converted Miles is:", km_to_miles(km), "Miles")

        elif choice == 3:
            fahrenheit = get_float("Enter the value in F: ")
            print("The Converted Celsius is:", f_to_c(fahrenheit), "C")

        elif choice == 4:
            celsius = get_float("Enter the value in Celsius: ")
            print("The converted Fahrenheit is:", c_to_f(celsius), "F")
        
        elif choice == 5:
            print("Bye, Have a good day!")
            break


main()