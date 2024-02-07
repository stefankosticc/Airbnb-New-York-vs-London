from pripremaPodataka import london_df
import plotly.graph_objects as go


# lon_sobe = london_df['room_type'].value_counts()
lon_naselja = london_df['neighbourhood'].value_counts().index
lon_sobe_po_naselju = london_df.groupby(['neighbourhood', 'room_type']).size()
print(lon_naselja)
print(lon_sobe_po_naselju)
