secret = 7
tries = 0
guesses = 5

while True:
    if guesses <= 1:
        print("You have", guesses, "Guess left")
    else:
        print("You have", guesses, "Guesses left")
    
    guess = int(input("Guess the Number: "))
    tries += 1
    guesses -= 1

    if guess == secret:
        print("You got the number!!!")
        print("Total tries was:", tries)
        break
    else:
        if guesses == 0:
            print("You are out of guesses")
            print("Secret Number is:", secret)
            break
        print("Try again")
        if guess < secret:
            print("Number is too low")
        else:
            print("Number is too high")