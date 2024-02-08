from pripremaPodataka import london_df
import matplotlib.pyplot as plt
from PIL import Image

lats = london_df['latitude'].values
lons = london_df['longitude'].values

slika = Image.open('data/London_mapa.jpg')

room_types = london_df['room_type'].value_counts()

colors = {
    'Entire home/apt': 'mediumseagreen',
    'Private room': 'gold',
    'Shared room': 'indigo',
    'Hotel room': 'red'
}
plt.style.use('seaborn-v0_8-whitegrid')
fig, (grafik1, grafik2) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("London: Prikaz Tipova Soba", fontsize=18)

grafik1.imshow(slika, extent=(-0.54, 0.4, 51.25, 51.75))
grafik1.scatter(lons, lats, c=london_df['room_type'].map(colors), s=5)

grafik2.plot(room_types.index, room_types.values, 'o-r')

plt.show()
