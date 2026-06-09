import pandas

data = pandas.read_csv("weather_data.csv")
print("Here's all the data read by pandas:")
print(data)
print("\nHere's just the temps:")
print(data["temp"])