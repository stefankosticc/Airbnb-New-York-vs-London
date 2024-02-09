from pripremaPodataka import ny_df
from plotly import offline
import plotly.graph_objs as go

ny_naselja = ny_df['neighbourhood_group'].value_counts()

data = [{
    'type': 'bar',
    'x': ny_naselja.index,
    'y': ny_naselja.values,
    'marker': {
        'color': 'navajowhite',
        'line': {'width': 1.5, 'color': 'burlywood'}
    },
}]

my_layout = {
    'title': 'New York: Broj Smeštaja Po Naselju',
    'yaxis': {'title': 'Frekvencija'},
    # 'width': 700,
    # 'height': 500
}
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='')

fig = go.Figure(data=data, layout=my_layout)

fig.show()


