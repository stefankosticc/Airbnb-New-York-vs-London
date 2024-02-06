from pripremaPodataka import ny_df
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from PIL import Image

lats = ny_df['latitude'].values
lons = ny_df['longitude'].values

slika = Image.open('data/New_York_City.png')
# plt.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
#
#
# room_types = ny_df['room_type'].value_counts()
#
# colors = {
#     'Entire home/apt': 'yellow',
#     'Private room': 'blue',
#     'Shared room': 'red'
# }
#
# plt.scatter(lons, lats, c=ny_df['room_type'].map(colors), s=5)
#
# plt.show()
#
# # MAPA NASELJA
# ny_naselja = ny_df['neighbourhood_group']
# boje_naselja = {
#     'Manhattan': 'red',
#     'Brooklyn': 'blue',
#     'Queens': 'yellow',
#     'Bronx': 'green',
#     'Staten Island': 'orange'
# }
#
# plt.imshow(slika, extent=(-74.258, -73.7, 40.49,40.92))
# plt.scatter(lons, lats, c=ny_naselja.map(boje_naselja), s=3)
#
# plt.show()

# CENA
ny_cena = ny_df['price'].values

boundaries = [0, 1000, 10000]
norm = BoundaryNorm(boundaries, ncolors=256)
plt.imshow(slika, extent=(-74.258, -73.7, 40.49, 40.92))
plt.scatter(lons, lats, c=ny_cena, norm=norm, cmap=plt.get_cmap('RdYlGn').reversed(), alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('cena')

plt.show()

