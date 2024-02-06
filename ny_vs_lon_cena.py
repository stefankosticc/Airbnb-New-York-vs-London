from pripremaPodataka import ny_df, london_df
import matplotlib.pyplot as plt

ny_cena = ny_df['price'].value_counts().index
london_cena = london_df['price'].value_counts().index

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.plot(ny_cena, c='red')
ax.plot(london_cena, c='blue')
# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()