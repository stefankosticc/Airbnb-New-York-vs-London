from pripremaPodataka import london_df
import matplotlib.pyplot as plt
from PIL import Image

lats = london_df['latitude'].values
lons = london_df['longitude'].values

slika = Image.open('data/London_mapa.jpg')

# MAPA NASELJA
lon_naselja = london_df['neighbourhood'].value_counts().index

# for i in range(0, len(lon_naselja)):
#     lon_naselja[i] = i

print(lon_naselja[0])
plt.imshow(slika, extent=(-0.54, 0.4, 51.25, 51.75))
plt.scatter(lons, lats, c=lon_naselja, cmap='inferno', s=3)

plt.show()
