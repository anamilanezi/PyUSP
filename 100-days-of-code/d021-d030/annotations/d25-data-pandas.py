# Working with CSV files

# with open("weather_data.csv") as data_file:
#     data = data_file.read().splitlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # Creates an onject that can be iterated
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))               # DataFrame
# print(type(data['temp']))       # Series

# Converting to native datatypes
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)

# Get the average with native Python
# average_temp = sum(temp_list) / len(temp_list)
# print(f"{average_temp:.2f}")

# Getting the average and max value from a column with Pandas
# print(data['temp'].mean())
# print(data['temp'].max())
#
# Get Data in Columns: case sensitive
# print(data["condition"])
# print(data.condition)

# Get Data in Row (two methods, same result)
# print(data[data['day'] == "Monday"])
# print(data[data.day == "Monday"])

# Get the day with the highest temperature:
# high_temp = data.temp.max()
# high_temp_day = data[data.temp == high_temp]
# print(high_temp)
#
# Select the monday row and then de condition
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_f = (monday_temp * (9/5)) + 32
#
# print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Muffin", "Lionel", "Tunico"],
    "scores": [99, 56, 72]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")