#Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code

print(f'Pssst, the solution is {chosen_word}')

display = []
for i in range(len(chosen_word)):
    display.append("_")


guess = input("Guess a letter: ").lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)