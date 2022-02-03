import random
while True:
    user_choice = input("Choose an option (rock, paper, scissors) or type 'done' to exit: ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    if user_choice == "done":
        break
    elif user_choice == computer_choice:
        print("Both players selected", user_choice, ". It's a tie.")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper cover rock! You lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper cover rock! You win!")
        else:
            print("Scissors cut paper! You lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")