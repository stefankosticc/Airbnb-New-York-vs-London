from pripremaPodataka import ny_df, london_df
import matplotlib.pyplot as plt

ny_sobe = ny_df['room_type'].value_counts().sort_values()
london_sobe = london_df['room_type'].value_counts().sort_values()
london_sobe = london_sobe.drop(['Hotel room'])

print(london_sobe)
fig, ax = plt.subplots()
ax.plot(ny_sobe.index, ny_sobe.values, c='yellow')
ax.plot(london_sobe.index, london_sobe.values, c='green')

plt.show()
