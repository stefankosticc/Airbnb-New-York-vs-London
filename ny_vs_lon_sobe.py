from pripremaPodataka import ny_df, london_df
import matplotlib.pyplot as plt

ny_sobe = ny_df['room_type'].value_counts().sort_values()
london_sobe = london_df['room_type'].value_counts().sort_values()
london_sobe = london_sobe.drop(['Hotel room'])

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(ny_sobe.index, ny_sobe.values, 'o-b', label='New York')
ax.plot(london_sobe.index, london_sobe.values, 'o-r', label='London')
ax.set_title('Poređenje Broja Soba')
ax.legend()
plt.show()
