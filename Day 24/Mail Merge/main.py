# Read the Letter
with open("Day 24/Mail Merge/Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# Read the Names
names = []
with open("Day 24/Mail Merge/Input/Names/invited_names.txt") as file:
    line = file.readline()
    while line:
        names.append(line.strip())
        line = file.readline()

# Replace [name] and create a new file
for name in names:
    letter = starting_letter.replace('[name]', name)
    print(letter)
    with open(f"Day 24/Mail Merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter)