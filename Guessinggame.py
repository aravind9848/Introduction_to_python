import random

secret_number = random.randint(1, 100)
attempts = 0
while attempts < 10:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

if guess != secret_number:
    print(f"Sorry, you've used all attempts. The secret number was {secret_number}.")