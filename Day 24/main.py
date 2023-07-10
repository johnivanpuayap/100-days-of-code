
# # Opening a file
# file = open("Day 24\my_file.txt")

# # Reading a file
# contents = file.read()
# print(contents)

# # Closing a file
# file.close()

# Another way to open the file without the need to close the file
with open("Day 24\my_file.txt") as file:
    contents = file.read()
    print(contents)