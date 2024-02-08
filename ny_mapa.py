from pripremaPodataka import ny_df
import matplotlib.pyplot as plt
from PIL import Image

lats = ny_df['latitude'].values
lons = ny_df['longitude'].values

slika = Image.open('data/New_York_City.png')

room_types = ny_df['room_type'].value_counts()

colors = {
    'Entire home/apt': 'mediumseagreen',
    'Private room': 'gold',
    'Shared room': 'orangered'
}

fig, (grafik1, grafik2) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("New York: Prikaz Tipova Soba", fontsize=18)

grafik1.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
grafik1.scatter(lons, lats, c=ny_df['room_type'].map(colors), s=5)

grafik2.pie(room_types.values, labels=room_types.index, autopct='%.0f%%', radius=0.8, colors=colors.values())

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

fig, ax = plt.subplots()
ax.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
for naselje in boje_naselja:
    deo = ny_df[ny_df['neighbourhood_group'] == naselje]
    ax.scatter(deo['longitude'], deo['latitude'], c=boje_naselja[naselje], s=5, label=naselje, edgecolors='black', linewidths=0.08)

# Podešavanje legende i naslova
ax.legend(title='Naselja', loc='upper left')
ax.set_title("New York: Zastupljenost Smeštaja Po Naseljima")

plt.show()


