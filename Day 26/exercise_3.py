# Load from file 1
with open("Day 26/file1.txt") as file:
    file_1 = [int(num.strip()) for num in file.readlines()]
    print(file_1)
# Load from file 2
with open("Day 26/file2.txt") as file:
    file_2 = [int(num.strip()) for num in file.readlines()]
    print(file_2)

# Compare similarity
result = [num for num in file_1 if num in file_2]
print(result)