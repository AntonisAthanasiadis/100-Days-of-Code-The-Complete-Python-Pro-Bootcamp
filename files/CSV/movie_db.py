import pandas as pd

#Create a database of movies using a Python dictionary
movie_data = {
    'Title': ['The Matrix', 'Inception', 'Shrek', 'Toy Story', 'Superbad',
              'The Hangover', 'Spirited Away', 'Interstellar', 'Parasite', 'Knives Out'],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Animation', 'Animation', 'Comedy',
              'Comedy', 'Animation', 'Sci-Fi', 'Thriller', 'Mystery'],
    'Rating': [8.7, 8.8, 7.9, 8.3, 7.6, 7.7, 8.6, 8.7, 8.5, 7.9],
    'Runtime': [136, 148, 90, 81, 113, 100, 125, 169, 132, 130] # in minutes
}

#Convert our dictionary into a pandas dataframe
df = pd.DataFrame(movie_data)

print("Welcome to your Movie Assistant!")

print("\n1. Current Movie Database:")
print(df)

print("\n2. Quick Database Stats:")
print(f"• Average Movie Rating: {df['Rating'].mean():.2f} / 10")
print(f"• Total watch time if you watched everything: {df['Runtime'].sum()} minutes")

#Let's find high-rated movies (rating > 8.0) that are relatively short (under 130 minutes)
print("\n3. Recommendation: High-rated, shorter watches (Rating > 8.0 & Runtime < 130m):")
short_masterpieces = df[(df['Rating'] > 8.0) & (df['Runtime'] < 130)]
print(short_masterpieces[['Title', 'Genre', 'Rating']])


#Find out what the highest score is for each genre
print("\n4. Top Rating achieved by Genre:")
print(df.groupby('Genre')['Rating'].max())