#######
# This shows the mpg.csv dataset as a spread out scatter plot
# that sends hoverData to another graph via callback, and to
# a Markdown component through a second callback.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
# print info and head() of the df
print(df.info())
print(df.head())


# Add a random "jitter" to model_year to spread out the plot
# Using jitter is preferential and is optional
df['year'] = df['model_year'] + random.randint(-4, 5, len(df))*0.10

app.layout = html.Div([
    html.Div([   # this Div contains our scatter plot
        dcc.Graph(
            id='mpg_scatter',
            figure={
                'data': [go.Scatter(
                    x=df['year']+1900,  # our "jittered" data. model_year is 70-82, so add 1900 to make it 1970-1982
                    y=df['mpg'],
                    text=df['name'],
                    hoverinfo='text',  # 'test'+'y'+'x' would also work. 'text' is the default.
                    mode='markers'
                )],
                'layout': go.Layout(
                    title='mpg.csv dataset',
                    xaxis={'title': 'model year'},
                    yaxis={'title': 'miles per gallon'},
                    hovermode='closest'
                )
            }
        )], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([  # this Div contains our output graph and vehicle stats
        dcc.Graph(
            id='mpg_line',
            figure={
                # The default is a 45 degree slopped line. As we click on different points, the line will change.
                'data': [go.Scatter(
                    x=[0, 1],
                    y=[0, 1],
                    mode='lines'
                )],
                'layout': go.Layout(
                    title='acceleration',
                    # l stands for 'left' margin. We are just making sure this graph is more snug with the first graph.
                    margin={'l': 0}
                )
            }
        ),
        dcc.Markdown(
            id='mpg_stats'
        )
    ], style={'width': '20%', 'height': '50%', 'display': 'inline-block'})
])


@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    # get the vehicle index from the hoverData
    # remember that the index is not actually a column in the df, but it is the index of the row in the df (unique row).
    v_index = hoverData['points'][0]['pointIndex']

    # calculate the slope of the line for the scatterplot on the right
    figure = {
        # iloc stands for 'integer location'. It is a pandas function that allows us to access a specific row in the df.
        'data': [go.Scatter(
            x=[0, 1],
            # Update the y value to match the acceleration of the vehicle we clicked on.
            # The slower the acceleration (the higher the number for acceleration), the flatter the line will be.
            y=[0, 60/df.iloc[v_index]['acceleration']],
            mode='lines',
            # Adjust the thickness of the line based on the number of cylinders.
            line={'width': 2*df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title=df.iloc[v_index]['name'],
            xaxis={'visible': False},
            yaxis={'visible': False, 'range': [0, 60/df['acceleration'].min()]},
            margin={'l': 0},
            height=300
        )
    }
    return figure


@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']

    # create the markdown string
    stats = """
        {} cylinders
        {}cc displacement
        0 to 60mph in {} seconds
        """.format(df.iloc[v_index]['cylinders'],
                   df.iloc[v_index]['displacement'],
                   df.iloc[v_index]['acceleration'])

    return stats


if __name__ == '__main__':
    app.run_server()
