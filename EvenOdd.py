import random

def main():
    number = random.randint(1, 10)
    guess = str(input("Guess a number is even or odd: "))
    if guess == "even":
        if number % 2 == 0:
            print("You are right!")
        else:
            print("You are wrong!")
    elif guess == "odd":
        if number % 2 == 1:
            print("You are right!")
        else:
            print("You are wrong!")
    else:
        print("Please enter even or odd.")

if __name__ == "__main__":
    main()

# Sudo code
# Generate a random number between 1 and 10
# Ask the user to guess a number
# If the user's guess is correct, tell them they're right
# Otherwise, tell them they're wrong and what the number was
# Keep asking the user to guess until they get it right
