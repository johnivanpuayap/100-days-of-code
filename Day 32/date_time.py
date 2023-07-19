import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

if year == 2023:
    print("Hello there!")

day_of_the_week = now.weekday()
print(day_of_the_week)


# Create a date
date_of_birth = dt.datetime(year=1998, month=1, day=20)
print(date_of_birth)