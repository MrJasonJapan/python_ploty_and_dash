#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# import plotly and pandas
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Create a DataFrame from  "flights" data
df = pd.read_csv('../data/flights.csv')
print(df.shape)
print(df.head())
print(df.columns)


# create data for a heatmap with "year" on the x-axis, "month" on the y-axis, and "passengers" as the z-axis.
# Use "jet" as the colorscale and share the y-axis across all subplots.
data = [go.Heatmap(
    x=df['year'],
    y=df['month'],
    z=df['passengers'],
    colorscale='Jet'
)]


# Define the layout
layout = go.Layout(
    title='Flights'
)


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution8.html')
