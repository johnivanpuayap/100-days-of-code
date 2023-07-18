# Read the Letter
with open("Day 24/Mail Merge/Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# Read the Names
names = []
with open("Day 24/Mail Merge/Input/Names/invited_names.txt") as file:
    names = file.readlines()

# Replace [name] and create a new file
for name in names:
    name = name.strip()
    letter = starting_letter.replace('[name]', name)
    with open(f"Day 24/Mail Merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter)