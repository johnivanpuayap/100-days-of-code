print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
count = int(input("How many people to split the bill? "))

bill_per_person = total / count * (1 + tip/100)
print(f"Each person should pay:{bill_per_person: .2f}")