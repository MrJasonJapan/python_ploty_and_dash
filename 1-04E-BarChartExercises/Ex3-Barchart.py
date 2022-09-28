#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file, and set the index to the first column:
df = pd.read_csv('../data/mocksurvey.csv', index_col=0)
print(df)


# create traces using a list comprehension:
# data = [go.Bar(x=df.index, y=df[col], name=col) for col in df.columns]

# create traces using a list comprehension, and make the bars horizontal:
data = [go.Bar(y=df.index, x=df[col], name=col, orientation='h') for col in df.columns]


# create a layout in stack mode
layout = go.Layout(title='Mock Survey Results', barmode='stack')


# Create a fig from data & layout:
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Ex3-BarChart.html')
