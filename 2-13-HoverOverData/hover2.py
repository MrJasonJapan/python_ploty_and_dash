import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64  # need this for our encode_image function

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')


# This function will encode an image into base64 format so the browser can display it.
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='wheels-plot',
            figure={
                'data': [
                    go.Scatter(
                        x=df['color'],
                        y=df['wheels'],
                        dy=1,
                        mode='markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(51,204,153)',
                            'line': {'width': 2}
                        }
                    )
                ],
                'layout': go.Layout(
                    title='Wheels & Colors Scatterplot',
                    xaxis={'title': 'Color'},
                    yaxis={'title': '# of Wheels', 'nticks': 3},
                    hovermode='closest'
                )
            }
        )], style={'width': '30%', 'float': 'left'}),

    html.Div([
        # Image component is used to display the image corresponding to the hovered data point.
        html.Img(id='hover-image', src='', height=300)
    ], style={'paddingTop': 35})
])


@app.callback(
    Output('hover-image', 'src'),
    [Input('wheels-plot', 'hoverData')])
def callback_image(hoverData):
    # grab x and y values from the hoverData object and assign them to wheel and color respectively.
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = '../data/images/'
    return encode_image(path+df[(df['wheels'] == wheel) &
                                (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
