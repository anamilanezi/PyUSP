import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# This would select all rows and columns with gray, cinnamon and black, and with len we can get the count
# gray_count = len(df[df["Primary Fur Color"] == "Gray"])
# cinnamon_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
# black_count = len(df[df["Primary Fur Color"] == "Black"])
#

# Get Primary Fur Color column
fur_color = df["Primary Fur Color"]

# From this column, get each color
gray = fur_color[fur_color == "Gray"]
cinnamon = fur_color[fur_color == "Cinnamon"]
black = fur_color[fur_color == "Black"]

# Get the count of each color
gray_count = gray.count()
cinnamon_count = cinnamon.count()
black_count = black.count()
# print(gray_count, cinnamon_count, black_count)

# Make a dict:
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Create a dataframe and export to a csv file
data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")