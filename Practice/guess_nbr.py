import random

secret_number = random.randint(1, 100)
max_attempts = 5
print("Guess the number between 1 to 100")
print(f"you have {max_attempts} attempts ")

for attempts in range(1, max_attempts + 1):
    guess = int(input(f"Attempts {attempts}: Your guess: "))

    if guess < secret_number:
        print("To low! Try again\n")
    elif guess > secret_number:
        print("To high! Try again")
    else:
        print(f"Congrats you guessed it in {attempts} attempts")
        break
else:
    print(f"game Over! The number was {secret_number}. Better luck next time ")