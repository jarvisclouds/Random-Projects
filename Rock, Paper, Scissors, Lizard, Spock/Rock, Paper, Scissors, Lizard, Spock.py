import random
while True:
    user_choice = input("Choose an option (rock, paper, scissors, lizard, spock) or type 'done' to exit: ").lower()
    possible_choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(possible_choices)

    if user_choice in possible_choices:
        if user_choice == "done":
            break

        elif user_choice == computer_choice:
            print("Both players selected", user_choice, ". It's a tie.")

        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            elif computer_choice == "paper":
                print("Paper covers rock! You lose!")
            elif computer_choice == "lizard":
                print("Rock crushes lizard! You win!")
            elif computer_choice == "spock":
                print("Spock vaporizes rock! You lose!")

        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            elif computer_choice == "scissors":
                print("Scissors cut paper! You lose!")
            elif computer_choice == "lizard":
                print("Lizard eats paper! You lose!")
            elif computer_choice == "spock":
                print("Paper disproves spock! You win!")

        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cut paper! You win!")
            elif computer_choice == "rock":
                print("Rock smashes scissors! You lose!")
            elif computer_choice == "lizard":
                print("Scissors decapitates lizard! You win!")
            elif computer_choice == "spock":
                print("Spock smashes scissors! You lose!")

        elif user_choice == "lizard":
            if computer_choice == "scissors":
                print("Scissors decapitates lizard! You lose!")
            elif computer_choice == "paper":
                print("Lizard eats paper! You win!")
            elif computer_choice == "rock":
                print("Rock crushes lizard! You lose!")
            elif computer_choice == "spock":
                print("Lizard poisons spock! You win!")

        elif user_choice == "spock":
            if computer_choice == "scissors":
                print("Spock smashes scissors! You win!")
            elif computer_choice == "paper":
                print("Paper disproves spock! You lose!")
            elif computer_choice == "lizard":
                print("Lizard poisons spock! You lose!")
            elif computer_choice == "rock":
                print("Spock vaporizes rock! You win!")
    else:
        print("Error, please use one of the given options.")