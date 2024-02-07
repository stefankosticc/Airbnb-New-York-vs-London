from pripremaPodataka import ny_df
import matplotlib.pyplot as plt

srednje_cene_po_naselju = ny_df.groupby('neighbourhood_group')['price'].mean()

x_values = srednje_cene_po_naselju.index
y_values = srednje_cene_po_naselju.values

print(plt.style.available)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.bar(x_values, y_values)

# Set chart title and label axes.
ax.set_title("Prosečne cene po naselju", fontsize=24)
ax.set_xlabel("Naselja", fontsize=14)
ax.set_ylabel("Cene", fontsize=14)

plt.show()