# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Adding an Exception in a FileNotFound Error

try:
    file = open("Day 30/a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
    print(value)
except FileNotFoundError:
    file = open("Day 30/a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")