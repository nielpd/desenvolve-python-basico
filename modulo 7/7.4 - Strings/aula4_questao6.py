import pandas as pd

fp = 'spotify-2023.csv'
df = pd.read_csv(fp, encoding='latin-1')

df = df[~df['track_name'].str.contains(r'"') & ~df['artist(s)_name'].str.contains(r'"')]

df_filtered = df[(df['released_year'] >= 2012) & (df['released_year'] <= 2022)]

top_tracks_per_year = []

for year in range(2012, 2023):
    year_data = df_filtered[df_filtered['released_year'] == year]
  
    top_track = year_data.loc[year_data['streams'].idxmax()]

    top_tracks_per_year.append([top_track['track_name'], top_track['artist(s)_name'], top_track['released_year'], top_track['streams']])

print(top_tracks_per_year)
