# # Using the normal way to open file

# with open("Day 25\weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# # Using csv library

# import csv

# with open("Day 25\weather-data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

#     print(temperatures)

# Using the pandas library
import pandas as pd

data = pd.read_csv('Day 25\weather-data.csv')
print(data)
print(data['temp'])