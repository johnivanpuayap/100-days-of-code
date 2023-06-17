import random
number = random.randint(1, 100)
lives = 0
HARD = 5
EASY = 10

def set_difficulty(difficulty):
    """
    Assign the number of lives given a difficulty.
    
    Parameters:
    difficulty: A string that could be 'easy' or 'hard'

    Returns:
    int: number of lives

    """
    if difficulty == 'easy':
        return EASY
    elif difficulty == 'hard':
        return HARD
    else:
        print("Not a valid option")
        return 0

def check_answer(guess, number, lives):
    """
    Checks if the guess is equal to the number. 

    Returns:
    int: number of lives if not equal or -1 when equal
    """
    if guess > 100 or guess < 1:
        print("Guess is out bounds. Try again.")
    elif guess > number:
        print("Too high.")
        lives -= 1
    elif guess < number:
        print("Too low.")
        lives -= 1
    else:
        print(f"You got it. The answer was {number}!")
        lives = -1
    
    return lives

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

lives = set_difficulty(difficulty)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    lives = check_answer(guess, number, lives)

    if lives == 0:
        print("You've run out of guesses, you lose.")
    elif lives > 0:    
        print("Guess again.")
