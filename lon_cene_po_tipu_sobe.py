from pripremaPodataka import london_df
import matplotlib.pyplot as plt

srednje_cene_po_sobi = london_df.groupby('room_type')['price'].mean()

tip_sobe = srednje_cene_po_sobi.index
prosecne_cene = srednje_cene_po_sobi.values

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
bars = ax.barh(tip_sobe, prosecne_cene, align='center', color='red')
ax.set_title('London: Prosečne cene Po Tipu Sobe')
ax.set_xlabel("Prosečne cene")

# dodajemo vrednosti svakog stuba
ax.bar_label(bars, color='black', fontweight='bold')
# zbog bolje vidljivosti prosirujemo x osu
plt.xlim(0, max(prosecne_cene) * 1.2)

plt.show()
