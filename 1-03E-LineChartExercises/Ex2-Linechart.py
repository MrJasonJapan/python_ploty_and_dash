#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY',
        'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

# Use list comprehension to create traces for the data list.
data = [go.Scatter(x=df['LST_TIME'], y=df[df['DAY'] == day]['T_HR_AVG'], mode='lines',
                   name=day) for day in days]

# pyo.plot(data)

# Another way to prepare the data, but using a for loop instead.
# data = []
# for day in days:
#     trace = go.Scatter(x=df[df['DAY'] == day]['LST_TIME'],y=df[df['DAY'] == day]['T_HR_AVG'], mode='lines', name = day)
#     data.append(trace)

# Yet another way to prepare the data, without the need for the days array at the top of this file.
# data = [{'x': df['LST_TIME'], 'y': df[df['DAY'] == day]
#          ['T_HR_AVG'], 'name': day} for day in df['DAY'].unique()]

# Define the layout
layout = go.Layout(title='Daily temp avgs')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
