from pripremaPodataka import london_df
import matplotlib.pyplot as plt
import seaborn as sns

kolone_za_brisanje = london_df.select_dtypes(exclude=['number']).columns

corr_lon_df = london_df.drop(columns=kolone_za_brisanje)

lon_corr_matrica = corr_lon_df.corr()

sns.heatmap(lon_corr_matrica, annot=True, cmap='cool', fmt=".2f")
plt.title('Korelacija London')
plt.show()
