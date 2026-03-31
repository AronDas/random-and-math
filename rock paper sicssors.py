import random
while True:
    user_input = input("Enter either rock, paper, or scissors no capitals:")
    computer_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_actions)

    print("You selected", user_input, "While the bot selected", computer_choice)

    if computer_choice == user_input:
        print("Its a tie!")
    elif computer_choice == "rock":
        if user_input == "paper":
            print("Paper beats rock, you win!")
    elif computer_choice == "rock":
        if user_input == "scissors":
            print("Rock smashes scissors. you lose")
    elif computer_choice == "scissors":
        if user_input == "rock":
            print("Rock smashes scossors. you win!")
    elif computer_choice == "scissors":
        if user_input == "paper":
            print("scissors cuts paper. you lose")
    elif computer_choice == "paper":
        if user_input == "scissors":
            print("scissors cuts paper, you win!")
    elif computer_choice == "paper":
        if user_input == "rock":
            print("Paper covers rock. you lose")
    play_again = input("Would you like to play again?:(Y/N)")
    if play_again != "Y":
        break