import random

#Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

#using randint
count = len(names)
choice = random.randint(0, count-1)
person_who_will_pay = names[choice]

print(f"{person_who_will_pay} is going to buy the meal today!")

#using choice
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to buy the meal today!")