import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

avg_temp = data["temp"].mean()
print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

print(data.condition)

print(data[data.day == "Monday"])

#Create a dataframe from scratch
data_dict = {
    "students": ["Tony", "Amy", "James"],
    "scores": [76, 56, 85]
}
data = pandas.DataFrame(data_dict)
print(data)