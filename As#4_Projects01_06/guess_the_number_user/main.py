import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 10)
print("I have selected a Secret number between 1 and 10. Can you guess it?")

while True:
    try:
        guess=int(input("Enter your guess: "))
        if guess < secret_number:
            print("Your guess is too low. Try again!")
        elif guess > secret_number:
            print("Your guess is too high. Try again!")
        else:
            print("Congratulations! You've guessed the secret number!")
            break
    except ValueError:
        print("Please enter a valid number from 1 to 10.")


