# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        if month == 2:
            return month_days[month-1] + 1
        return month_days[month-1]
    else:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
if month > 12:
    print("There are only 12 months!")
elif month < 1:
    print("Month cannot be 0 or negative")
else:
    days = days_in_month(year, month)
    print(days)