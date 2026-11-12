def get_hint(guess, secret):
    if guess > secret:
        return "High"
    elif guess < secret:
        return "Low"
    elif guess == secret:
        return "Correct" 


def play_game(secret, max_guesses):
    tries = 0
    while True:
        num = int(input("Guess the number: "))
        answer = get_hint(num, secret)

        tries += 1
        if answer == "Correct":
            print("Correct with", tries, "tries!")
            break


        else:
            max_guesses -= 1
            if max_guesses == 0:
                print("You're out of tries! and the number is:", secret)
                break



            elif answer == "High":
                print("Answer is High")
            elif answer == "Low":
                print("Answer is Low")
            
            if max_guesses <= 1:
                print("You have your last Guess left")
            else:
                print("You have",max_guesses, "Guesses left")
    

while True:
    play_game(7, 5)

    play = input("Want to Play again [Y/N]?: ")
    if play == "Y" or play == "y":
        continue
    else:
        print("Thanks for playing!")
        break
    