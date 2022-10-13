#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Import ploty and pandas
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a DataFrame from the .csv file, and replace horpower values of ? to null.
df = pd.read_csv('../data/mpg.csv')
print(df)

# create data with scatter plot, x=weight, y=mpg, text=name, with a mode of markers
data = [go.Scatter(
    x=df['weight'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    # set the marker size based on accelleration, and show a color scale based on acceleration, with a title of acceleration
    marker=dict(size=1.5*df['acceleration'], color=df['acceleration'],
                showscale=True, colorbar={'title': 'Acceleration'})
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Vehicle weight vs. Miles per gallon',
    xaxis=dict(title='weight'),
    yaxis=dict(title='mpg'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_excercise.html')
