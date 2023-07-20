old_list = [1, 2, 3]

# Using List Comprehensions
new_list = [i+1 for i in old_list]

print(new_list)

# Using Map and Lambda Function
new_list = list(map(lambda x: x+1, old_list))

print(new_list)
