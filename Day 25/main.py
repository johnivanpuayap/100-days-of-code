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

# data = pd.read_csv('Day 25\weather-data.csv')

# print(data)
# print(data['temp'])

# # Converting DataFrame to dict
# data_dict = data.to_dict()
# print(data_dict)

# # Convert Series to list
# temperatures = data["temp"]
# temp_list = temperatures.to_list()
# print(temp_list)


# # Calculate the Average Temperature
# print(f"The average temperature is {temperatures.mean()}.")

# # Print the Maximum Value of Temperatures
# print(f"The maximum temperature is {temperatures.max()}.")

# # Get Data in Columns
# print(data.condition)

# # Get Data in Rows
# print(data[data.day == 'Monday'])

# # Get the Data in Rows wher temperature is Max
# max_temperature = data.temp.max()
# print(data[data.temp == max_temperature])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# monday_temp_F = monday.temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a DataFrame from scratch
data_dict = {
    "Students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("Day 25/new_data.csv")

