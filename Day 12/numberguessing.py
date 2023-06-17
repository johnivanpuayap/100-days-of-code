import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.choice(range(1, 101))
lives = 0

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print("Not a valid option")

while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > 100 or guess < 1:
        print("Guess is out bounds. Try again.")
    elif guess > number:
        print("Too high.")
        lives -= 1
    elif guess < number:
        print("Too low.")
        lives -= 1
    else:
        print("You guessed it. You win!")
        break
    
    if lives == 0:
        print("You've run out of guesses, you lose.")
    else:    
        print("Guess again.")


