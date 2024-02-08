from pripremaPodataka import ny_df, london_df
import matplotlib.pyplot as plt

lon_srednje_cene_po_sobi = london_df.groupby('room_type')['price'].mean()
lon_srednje_cene_po_sobi = lon_srednje_cene_po_sobi.drop(['Hotel room'])
lon_tip_sobe = lon_srednje_cene_po_sobi.index
lon_prosecne_cene = lon_srednje_cene_po_sobi.values

ny_srednje_cene_po_sobi = ny_df.groupby('room_type')['price'].mean()
ny_tip_sobe = ny_srednje_cene_po_sobi.index
ny_prosecne_cene = ny_srednje_cene_po_sobi.values

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(ny_tip_sobe, ny_prosecne_cene, 'o-b', label='New York')
ax.plot(lon_tip_sobe, lon_prosecne_cene, 'o-r', label='London')
ax.set_title('Poređenje Prosečnih Cena Po Tipu Sobe')
ax.legend()
plt.show()
