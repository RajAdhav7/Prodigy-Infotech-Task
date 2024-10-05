import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
