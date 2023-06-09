#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for i in range(0, nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]

for i in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

for i in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

#not using while loop
for i in range(0, nr_letters + nr_symbols + nr_numbers):
    choice = random.choice(["letters", "numbers", "symbols"])

    if choice == "letters":
        if nr_letters > 0:
            password += letters[random.randint(0, len(letters) - 1)]
            nr_letters -= 1
        else:
            choice = random.choice(["numbers", "symbols"])

            if choice == "numbers":
                if nr_numbers > 0:
                    password += numbers[random.randint(0, len(numbers) - 1)]
                    nr_numbers -= 1
                else:
                    password += symbols[random.randint(0, len(symbols) - 1)]
                    nr_symbols -= 1
            else:
                if nr_symbols > 0:
                    password += symbols[random.randint(0, len(symbols) - 1)]
                    nr_symbols -= 1
                else:
                    password += numbers[random.randint(0, len(numbers) - 1)]
                    nr_numbers -= 1
    elif choice == "numbers":
        if nr_numbers > 0:
            password += numbers[random.randint(0, len(numbers) - 1)]
            nr_numbers -= 1
        else:
            choice = random.choice(["letters", "symbols"])

            if choice == "letters":
                if nr_letters > 0:
                    password += letters[random.randint(0, len(letters) - 1)]
                    nr_letters -= 1
                else:
                    password += symbols[random.randint(0, len(symbols) - 1)]
                    nr_symbols -= 1
            else:
                if nr_symbols > 0:
                    password += symbols[random.randint(0, len(symbols) - 1)]
                    nr_symbols -= 1
                else:
                    password += letters[random.randint(0, len(letters) - 1)]
                    nr_letters -= 1
    else:
        if nr_symbols > 0:
            password += symbols[random.randint(0, len(symbols) - 1)]
            nr_symbols-= 1
        else:
            choice = random.choice(["letters", "numbers"])
            if choice == "letters":
                if nr_letters > 0:
                    password += letters[random.randint(0, len(letters) - 1)]
                    nr_letters -= 1
                else:
                    password += numbers[random.randint(0, len(numbers) - 1)]
                    nr_numbers -= 1
            else:
                if nr_numbers > 0:
                    password += numbers[random.randint(0, len(numbers) - 1)]
                    nr_numbers -= 1
                else:
                    password += letters[random.randint(0, len(letters) - 1)]
                    nr_letters -= 1

# using while loop
# choices = [letters, numbers, symbols]s
# numbers = [nr_letters, nr_numbers, nr_symbols]
# for i in range(0, nr_letters + nr_symbols + nr_numbers):
#     while True:
#         choice = random.randint(0, 2)
#         if numbers[choice] != 0:
#             password += choices[choice][random.randint(0, len(choices[choice]) - 1)]
#             numbers[choice] -= 1
#             break
#         else:
#             continue

print(password)