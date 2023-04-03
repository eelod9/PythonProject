import csv
import pandas
#data = []
#with open("./readwrite/csv read/weather_data.csv","r") as file:
#    data  = file.readlines()
#print(data)
'''
with open("./readwrite/csv read/weather_data.csv","r") as file:

    data = csv.reader(file)
    temperatures = []
    print(data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
'''

data = pandas.read_csv("./readwrite/csv read/weather_data.csv")


data_dict = data.to_dict()
temp = data["temp"].to_list()
average_temp = data["temp"].mean()
max_temp = data["temp"].max()
#print(data[data.temp ==data.temp.max()])

#get data in row
Mondaytemp = data[data.day =="Monday"].temp

#celsius to fahrenheit
Mondaytemp_f =(Mondaytemp * (9/5) +32)
print(Mondaytemp_f)

#create a dataframe from scratch
data1_dict = {
    "students": ["Ella", "Clara", "DJ"],
    "scores": [76, 56, 65]
}
data1 = pandas.DataFrame(data1_dict) 
data1.to_csv("./readwrite/csv read/new_data.csv")
print(data1)