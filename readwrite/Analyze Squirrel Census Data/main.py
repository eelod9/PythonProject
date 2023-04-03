import pandas

data = pandas.read_csv("./readwrite/Analyze Squirrel Census Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#filter data
data1 = len(data[data["Primary Fur Color"] == "Gray"])
data2 = len(data[data["Primary Fur Color"] == "Cinnamon"])
data3 = len(data[data["Primary Fur Color"] == "Black"])

data1_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [data1, data2, data3]
}
final = pandas.DataFrame(data1_dict) 
print(final)

final.to_csv("./readwrite/Analyze Squirrel Census Data/new_data.csv")

