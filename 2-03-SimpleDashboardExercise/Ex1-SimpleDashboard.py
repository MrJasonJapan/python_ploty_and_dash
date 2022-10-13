#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# import dash related libraries, plotly, and pandas
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# Launch the application:
app = dash.Dash()


# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/OldFaithful.csv')
# print the df shape, head, and columns
print(df.shape)
print(df.head())
print(df.columns)


# Create a Dash layout with a single scatterplot graph with 'X' and 'Y' on the axes:
app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode='markers',
                    marker={
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title='Old Faithful Eruption Intervals v Durations',
                xaxis={'title': 'Duration of eruption (minutes)'},
                yaxis={'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )
        }
    )
])


# Add the server clause:
if __name__ == '__main__':
    app.run_server()
