import pandas as pd

#Create the data
practice_log = {
    'Day': ['Mon', 'Tue', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Instrument': ['Guitar', 'Piano', 'Piano', 'Guitar', 'Rest', 'Guitar'],
    'Minutes': [40, 60, 45, 30, 0, 90],
    'Notes_Learned': [4, 8, 3, 2, 0, 12]
}

#turn the data into a dataframe
df = pd.DataFrame(practice_log)

print("Weekly Practice Log")
print(df)

#Divide Minutes by Notes_Learned and round to 2 decimal places
df['Minutes_Per_Note'] = (df['Minutes'] / df['Notes_Learned']).round(2)

#Fix the rest day row where notes learned is 0, setting the result to 0 instead of NaN
df.loc[df['Notes_Learned'] == 0, 'Minutes_Per_Note'] = 0

print("\nAdded Minutes Per Note column to track focus:")
print(df[['Day', 'Instrument', 'Minutes_Per_Note']])

print("\nFinal Weekly Wrap up")

#calculate the total time
total_time = df['Minutes'].sum()

#find the most common instrument name
favorite_instrument = df['Instrument'].mode()[0]

print(f"Total time spent practicing this week: {total_time:.1f} minutes")
print(f"Most practiced instrument this week: {favorite_instrument}")