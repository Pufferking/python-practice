import pandas

#Counting number of squirrels with specific color from the Squirrel census using pandas library
# and making a new csv file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Color": ["Gray", "Black", "Red"],
    "Count": [gray, black, red]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
