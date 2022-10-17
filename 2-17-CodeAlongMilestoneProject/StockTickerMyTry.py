#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# import dash, dash input/output/State, ploty, numpy, and pandas, and pandas datareader
from click import style
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

from requests import head

# create the dash app
app = dash.Dash()

# get a list of tickers from the NASDAQcompanylist.csv file
nsdq = pd.read_csv('../data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
print(nsdq.head())

# create the dropdown options based on the ndsq Symbols
options = []
for tic in nsdq.index:
    options.append({'label': '{} {}'.format(tic, nsdq.loc[tic]['Name']), 'value': tic})

print(options)

# Create the app layout, with a header, a dropdown component, date-picker, and submit button on the same row.
app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Select a stock symbol:', style={'paddingRight': '30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'],
            multi=True
        ),
    ], style={'display': 'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2015, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        ),
    ], style={'display': 'inline-block', 'marginLeft': '30px'}),

    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize': 24, 'marginLeft': '30px'}
        ),
    ], style={'display': 'inline-block'}),

    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1, 2], 'y': [3, 1]}
            ],
            'layout': {'title': 'Default Title'}
        }
    )
])


# Create a callback function that updates the graph based based on the input date range, and stock ticker symbol.
# Set the title of the graph to the stock ticker symbol.
@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'), State('my_date_picker', 'start_date'), State('my_date_picker', 'end_date')]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    # create data traces for each stock_ticker.
    traces = []
    for tic in stock_ticker:
        # Obtain a df based on the start and end date, and the stock ticker symbol.
        df = web.DataReader(tic, 'yahoo', start=start_date, end=end_date)
        traces.append({'x': df.index, 'y': df['Close'], 'name': tic})

        # print info about the current df
        print(df.info())
        print(df.head())

    # create the figure based on the traces. Join all of the stock_ticker items to make a single title.
    fig = {
        'data': traces,
        'layout': {'title': ', '.join(stock_ticker) + ' Closing Prices'}
    }

    return fig


# start the app server
if __name__ == '__main__':
    app.run_server()
