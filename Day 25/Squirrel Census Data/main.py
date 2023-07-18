import pandas as pd

data = pd.read_csv('Day 25\\Squirrel Census Data\\2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')


gray_squirrels = data[data["Primary Fur Color"] == 'Gray']
number_gray_squirrels = len(gray_squirrels)


red_squirrel = data[data["Primary Fur Color"] == 'Cinnamon']
number_red_squirrels = len(red_squirrel)

black_squirrel = data[data["Primary Fur Color"] == 'Black']
number_black_squirres = len(black_squirrel)

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [number_gray_squirrels, number_red_squirrels, number_black_squirres]
}

data = pd.DataFrame(squirrel_dict)
data.to_csv("Day 25\\Squirrel Census Data\\squirrel_count.csv")