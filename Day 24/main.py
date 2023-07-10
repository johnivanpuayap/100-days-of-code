
# # Opening a file
# file = open("Day 24\my_file.txt")

# # Reading a file
# contents = file.read()
# print(contents)

# # Closing a file
# file.close()

# Another way to open and read the file without the need to close the file
with open("Day 24\my_file.txt") as file:
    contents = file.read()
    print(contents)

# Another way to write the file without the need to close the file

# write
with open("Day 24\my_file.txt", mode='w') as file:
    file.write("\nNew text.")

# append
with open("Day 24\my_file.txt", mode='a') as file:
    file.write("\nNew text.")