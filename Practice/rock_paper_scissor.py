import random

choices = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    computer_choice = random.choice(choices)
    print(f"I choose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (computer_choice == "scissors" and user_choice == "paper") \
         or (computer_choice == "rock" and user_choice == "scissors") \
         or (computer_choice == "paper" and user_choice == "rock"):
        print("You Lose!")
        computer_score += 1
    elif (user_choice == "rock" and computer_choice == "scissors") \
         or (user_choice == "scissors" and computer_choice == "paper") \
         or (user_choice == "paper" and computer_choice == "rock"):
        print("You Win!")
        player_score += 1
    else:
        print("Invalid Input, try again.")
        continue  # skip score check if invalid input

    print(f"Score: Computer {computer_score} vs You {player_score}")

    # Check if someone reached 5
    if computer_score == 5:
        print(f"Game Over! You Lose. Final score: Computer {computer_score} vs You {player_score}")
        break
    elif player_score == 5:
        print(f"Congratulations! You Win. Final score: Computer {computer_score} vs You {player_score}")
        break

    # Ask to continue
    cont = input("Wanna continue? (y/n): ").strip().lower()
    if cont == "n":
        print(f"Thank you for playing! Final score: Computer {computer_score} vs You {player_score}")
        break