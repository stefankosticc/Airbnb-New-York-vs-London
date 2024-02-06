import pandas as pd


# NEW YORK

original_ny_df = pd.read_csv("data/AB_NYC_2019.csv")

# Uklanjamo kolone koje nam nisu potrebne za dalju analizu a sadrže prazne ćelije
ny_df = original_ny_df.drop(columns=['last_review', 'reviews_per_month'], axis=1)

# Dodajemo koloni 'name' i kolini 'host_name' vrednosti za prazne ćelije
# izbacuje gresku za inplace u novijoj Pandas verziji pa koristimo sledeći način
ny_df['name'] = ny_df['name'].fillna('Unknown')
ny_df['host_name'] = ny_df['host_name'].fillna('Unknown')

# print(ny_df[ny_df.duplicated()].sum())
# nema duplikata

# LONDON

original_london_df = pd.read_csv("data/london-data.csv")

# Uklanjamo kolone koje nam nisu potrebne za dalju analizu a sadrže prazne ćelije
london_df = original_london_df.drop(columns=['last_review', 'reviews_per_month', 'license', 'neighbourhood_group'], axis=1)

# Dodajemo koloni 'name' i kolini 'host_name' vrednosti za prazne ćelije
# izbacuje gresku za inplace u novijoj Pandas verziji pa koristimo sledeći način
london_df['name'] = london_df['name'].fillna('Unknown')
london_df['host_name'] = london_df['host_name'].fillna('Unknown')

# print(ny_df[ny_df.duplicated()].sum())
# nema duplikata

# print(ny_df.info())

