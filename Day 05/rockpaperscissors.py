rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0  or user_choice >= 3: 
    print(images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: " + images[computer_choice])

    if user_choice == 0:
        if computer_choice == 0:
            print("It's a Draw!")
        elif computer_choice == 1:
            print("You Lose!")
        else:
            print("You Win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win!")
        elif computer_choice == 1:
            print("It's a Draw!")
        else:
            print("You Lose!")
    else:
        if computer_choice == 0:
            print("You Lose!")
        elif computer_choice == 1:
            print("You Win!")
        else:
            print("It's a Draw!")
else:
    print("You entered an invalid number. You lose!")

