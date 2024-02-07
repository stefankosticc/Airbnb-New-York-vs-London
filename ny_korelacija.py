from pripremaPodataka import ny_df
import matplotlib.pyplot as plt
import seaborn as sns

kolone_za_brisanje = ny_df.select_dtypes(exclude=['number']).columns

corr_ny_df = ny_df.drop(columns=kolone_za_brisanje)

ny_corr_matrica = corr_ny_df.corr()

sns.heatmap(ny_corr_matrica, annot=True, cmap='inferno_r', fmt=".2f")
plt.title('Korelacija New York')
plt.show()
