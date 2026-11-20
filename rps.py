import random


def decision(user, computer):
    if (user == "rock") and (computer == "scissor"):
        return "win"
    elif (user == "scissor") and (computer == "paper"):
        return "win"
    elif (user == "paper") and (computer == "rock"):
        return "win"
    elif user == computer:
        return "tie"       
    else:
        return "lose"


def user_input(prompt):
    while True:    
        value = input(prompt).lower()
        if (value == "rock") or (value == "paper") or (value == "scissor") or (value == "quit"):
            return value
        else:
            print("Invalid Answer, Try again!")


def main():
    user_score = 0
    comp_score = 0
    choices = ["rock", "paper", "scissor"]

    while True:
        answer = user_input("Rock, Paper, or Scissor?: ")
        
        if answer == "quit":
            print("Final Scores: You -", user_score, ", Computer -", comp_score)
            print("Thank you for playing!")
            break

        computer = random.choice(choices)
        print("Computer Chose:", computer)

        output = decision(answer, computer)

        if output == "win":
            user_score += 1
            print("You Won")
        elif output == "lose":
            comp_score += 1
            print("You Lost")
        elif output == "tie":
            print("It's a tie")
        print("Score: You -", user_score, ", Computer -", comp_score)
        print()


main()

print(decision("rock", "scissor"))      # win
print(decision("scissor", "paper"))     # win
print(decision("paper", "rock"))        # win
print(decision("rock", "paper"))        # lose
print(decision("scissor", "rock"))      # lose
print(decision("paper", "scissor"))     # lose
print(decision("rock", "rock"))         # tie
print(decision("paper", "paper"))       # tie
print(decision("scissor", "scissor"))   # tie