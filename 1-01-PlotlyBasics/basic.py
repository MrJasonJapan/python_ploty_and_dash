# basic.py
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(41,204,153)',
        symbol='pentagon',
        line={'width': 2}
    ))]

layout = go.Layout(
    title={'text': 'My First Plotly Plot', 'x': 0.5, 'xanchor': 'center'},
    xaxis={'title': 'MY X AXIS'},
    yaxis=dict(title='MY Y AXIS'),
    hovermode='closest'
)

fig = go.Figure(data=data, layout=layout)

# Another way to center the title.
# fig.update_layout(title_text="My First Plotly Plot", title_x=0.5)

pyo.plot(fig, filename='scatter.html')
