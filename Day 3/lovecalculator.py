print("Welcome to the Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined = name1.lower() + name2.lower()

score = 0

score += combined.count("t")
score += combined.count("r")
score += combined.count("u")
score += combined.count("e")
score *= 10
score += combined.count("l")
score += combined.count("o")
score += combined.count("v")
score += combined.count("e")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")