def deposit(amount, balance):
    final = amount + balance
    return final
    

def withdraw(amount, balance):
    final = balance - amount
    return final 


def get_choice():
    while True:
        try:
            choice = int(input("Choose your option: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Wrong Number")
        except ValueError:
            print("Invalid, Try again")


def get_float(prompt):
    while True:
        try:
            check = float(input(prompt))
            if check <= 0:
                print("Amount must be positive")
            else:
                return check
        except ValueError:
            print("Wrong value, try again!")


def show_menu():
    print()
    print("=== Bank Menu ===")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    print()


def main():
    balance = 100.0

    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            print(balance, "USD")

        elif choice == 2:
            depo_value = get_float("Enter the amount to Deposit: ")
            balance = deposit(depo_value, balance)
            print("Deposited", depo_value, "Balance is:", balance, "USD")
            
        elif choice == 3:
            withdraw_value = get_float("Enter the amount to Withdraw: ")

            if balance >= withdraw_value:
                balance = withdraw(withdraw_value, balance)
                print("Withdrawn", withdraw_value, "Balance is:" ,balance, "USD")

            else:   
                print("Insufficient Funds, Your Balance is: ", balance)
        
        elif choice == 4:
            print("Have a good day!")
            break


main()