names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Use Dictionary Comprehension for lists
import random
students_score = {name:random.randint(0, 100) for name in names}
print(students_score)

# Use Dictionary Comprehension for dictionaries
passed_students = {key:value for (key, value) in students_score.items() if value >= 70}
print(passed_students)


