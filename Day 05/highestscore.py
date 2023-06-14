# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest = 0

for score in student_scores:
  if score > highest:
    highest = score

# this activity doesn't allow us to use the max function but if you can just use this one line instead of a for loop
# highest = max(student_scores)

print(f"The highest score in the class is: {highest}")