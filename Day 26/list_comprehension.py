
old_list = [1, 2, 3]
# Using List Comprehensions
new_list = [i+1 for i in old_list]
print(new_list)

# Using Map and Lambda Function
new_list = list(map(lambda x: x+1, old_list))
print(new_list)


# Making a list of letters from a string using list comprehensions
name = "John Ivan"
name_list = [letter for letter in name]
print(name_list)

# Sequences in Python
# list
# range
# tuple
# string

# Using range as a lst in list comprehensions
number_list = [n*2 for n in range(1,5)]
print(number_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Using Conditional List Comprehension
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Using Filter and Lambda Function
short_names = list(filter(lambda x: len(x) <=4, names))
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)