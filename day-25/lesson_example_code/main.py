# import csv
#
# temperatures = []
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# Can access a column either like calling a list, or like an object
# print(data["temp"].mean())
# print(data.temp.max())
#
# # To get the row with data from Monday, I need to specify which column am I specifying for (here the day column),
# # then checking for the respective value.
# print(data[data.day == "Monday"])
#
# # Print row whose temp is the maximum
# print(data[data.temp == data.temp.max()])

# # After retrieving a row, we can also get a specific item from its columns
# # Get the row data for Monday
# monday = data[data.day == "Monday"]
# # Print the condition attribute value for the Monday row
# print(monday.condition)
#
# # By adding the int typecasting, we get the pure number and not the series format of printing (0 temp)s
# fahrenheit = (int(monday.temp) * 9/5) + 32
#
# print(fahrenheit)

data_dict = {
    "students": ["Bob", "Max", "Tim"],
    "scores": [74, 92, 48],
}

student_data = pandas.DataFrame(data_dict)
print(student_data)

student_data.to_csv("student_data.csv")