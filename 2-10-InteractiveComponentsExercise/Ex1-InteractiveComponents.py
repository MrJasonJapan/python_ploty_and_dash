#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# import dash, plotly and pandas
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()


# Create a dash layout with two divs inside. Style the app with a padding of 10px.
# The first div has a range slider from -5 to 5, with two endpoints, and only takes up 50% of the screen.
# The second div will be text, showing the product of the endpoints.
app.layout = html.Div([
    html.Div([
        dcc.RangeSlider(
            id='range-slider',
            min=-5,
            max=5,
            step=1,
            value=[-3, 4]
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div(id='product')
], style={'padding': 10})


@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
# Create a Dash callback function that will with 'range-slider' as input and 'product' as output.
# The callback will take the endpoints of the range slider and multiply them together.
def update_output_div(value_list):
    return 'The product of the endpoints is {}'.format(value_list[0] * value_list[1])


# Add the server clause:
if __name__ == '__main__':
    app.run_server()
