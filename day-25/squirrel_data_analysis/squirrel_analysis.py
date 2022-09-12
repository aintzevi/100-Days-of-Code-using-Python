import pandas

# Get data from csv file, already with separation based on the column name
squirrel_data = pandas.read_csv("data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Pick squirrels based on the primary fur colory column
gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

gray_squirrel_count = len(gray_squirrels)
cinnamon_squirrel_count = len(cinnamon_squirrels)
black_squirrel_count = len(black_squirrels)

# print(gray_squirrel_count)
# print(cinnamon_squirrel_count)
# print(black_squirrel_count)

# Create a data dictionary based on the counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

# Create a dataframe out of the dictionary
df = pandas.DataFrame(data_dict)
# Write data to a csv file
df.to_csv("data/squirrel_count.csv")
