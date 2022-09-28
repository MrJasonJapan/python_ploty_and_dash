#######
# A basic bar chart showing the total number of
# 2018 Winter Olympics Medals won by Country.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/2018WinterOlympics.csv')
print(df)

# create traces
trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold',
                marker={'color': '#FFD700'})
trace2 = go.Bar(x=df['NOC'], y=df['Silver'],
                name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'],
                name='Bronze', marker={'color': '#CD7F32'})

data = [trace1, trace2, trace3]

# stacked bar chart layout
layout = go.Layout(
    title='2018 Winter Olympics Medals by Country', barmode='stack'
)

# layout = go.Layout(
#     title='2018 Winter Olympic Medals by Country'
# )

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')
