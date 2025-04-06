import random
print("Welcome to the Number Guessing Game!")


low =1 
high = 10

print(f"Think of a number between {low} and {high}. Computer will try to guess it.")

if low <= high:
    guess = random.randint(low, high)
    print("Computer's guess is:", guess)

    while True:
        feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == "H":
            high = guess - 1
            guess = random.randint(low, high)
            print("Computer's new guess is:", guess)
        elif feedback == "L":
            low = guess + 1
            guess = random.randint(low, high)
            print("Computer's new guess is:", guess)
        elif feedback == "C":
            print("Yay! Computer guessed your number.")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")

if low > high:
    print("Invalid range. Please ensure the lower limit is less than or equal to the upper limit.")    
            