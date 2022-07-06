def start():

    import random
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            # code by Dev Varun
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

start()

def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()

restart_and_exit()

xyz_pro_plus = 1

while (xyz_pro_plus < 2):
    restart_and_exit()
