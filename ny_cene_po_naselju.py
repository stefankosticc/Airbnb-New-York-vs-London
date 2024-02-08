from pripremaPodataka import ny_df
import plotly.graph_objs as go

srednje_cene_po_naselju = ny_df.groupby('neighbourhood_group')['price'].mean()

x_values = srednje_cene_po_naselju.index
y_values = srednje_cene_po_naselju.values

data = [{
    'type': 'bar',
    'x': x_values,
    'y': y_values,
    'marker': {
        'color': 'cornflowerblue',
        'line': {'width': 1.5, 'color': 'royalblue'}
    },
}]

my_layout = {
    'title': 'New York: Prosečna Cena Po Naselju',
    'yaxis': {'title': 'Cene'},
    'width': 700,
    'height': 500,
}

fig = go.Figure(data=data, layout=my_layout)
fig.show()
