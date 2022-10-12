#######
# A bubble chart is simply a scatter plot
# with the added feature that the size of the
# marker can be set by the data.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mpg.csv', na_values={'horsepower': '?'})

# filter the dataframe where 'hoursepower' is numeric, and change the "horsepower" column to int64 type
# df = df[df['horsepower'].apply(lambda x:x.isnumeric())]
# df['horsepower'] = df['horsepower'].astype('int64')

# start with a normal scatter plot
data = [go.Scatter(
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],  # text displayed when hovering over a bubble
    mode='markers',
    # set the marker size. use a multiplier to make the bubbles more visible.
    # marker=dict(size=1.5*df['cylinders'])
    # set the marker size. divide by 100 to make the bubbles more visible. Add color based on the number of cylinders. Set a scale and set the name to "cylinders."
    marker=dict(size=df['weight']/100, color=df['cylinders'],
                showscale=True, colorbar={'title': 'Cylinders'})
)]

# setup the layout
layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis=dict(title='horsepower'),  # x-axis label
    yaxis=dict(title='mpg'),        # y-axis label
    hovermode='closest'
)

# setup the figure and plot
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
