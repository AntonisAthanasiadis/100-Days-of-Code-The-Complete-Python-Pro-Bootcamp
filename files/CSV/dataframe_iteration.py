import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)


for index, row in df.iterrows():
    print(f"Index: {index} | Name: {row['Name']} lives in {row['City']}")

for row in df.itertuples():
    # You access columns using the dot (.) notation
    print(f"ID: {row.Index} | {row.Name} is {row.Age} years old")