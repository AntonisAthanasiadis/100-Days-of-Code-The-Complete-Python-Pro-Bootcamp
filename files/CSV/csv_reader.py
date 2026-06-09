# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if "temp" not in row[1]:
            temperatures.append(row[1])
            print(row)

    print(f"The temperatures are: {temperatures}")