#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# import plotly and pandas
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')
print(df)


# create a data variable with one Histogram using the 'length' field, with a range of 0 to 1, and a bin size of 0.02
data = [
    go.Histogram(
        x=df['length'],
        xbins=dict(start=0, end=1, size=0.02)
    )
]

# add a layout
layout = go.Layout(
    title='Histogram of the length field from the Abalone dataset'
)


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution6.html')
