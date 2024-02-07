from pripremaPodataka import ny_df
import matplotlib.pyplot as plt
from PIL import Image

lats = ny_df['latitude'].values
lons = ny_df['longitude'].values

slika = Image.open('data/New_York_City.png')

room_types = ny_df['room_type'].value_counts()

colors = {
    'Entire home/apt': 'yellow',
    'Private room': 'blue',
    'Shared room': 'red'
}

fig, (grafik1, grafik2) = plt.subplots(1,2)

grafik1.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
grafik1.scatter(lons, lats, c=ny_df['room_type'].map(colors), s=5)

grafik2.pie(room_types.values, labels=room_types.index, autopct='%.0f%%', radius=0.8)

plt.show()

# MAPA NASELJA
ny_naselja = ny_df['neighbourhood_group']
boje_naselja = {
    'Manhattan': 'red',
    'Brooklyn': 'blue',
    'Queens': 'yellow',
    'Bronx': 'green',
    'Staten Island': 'orange'
}

plt.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
plt.scatter(lons, lats, c=ny_naselja.map(boje_naselja), s=3)

plt.show()


