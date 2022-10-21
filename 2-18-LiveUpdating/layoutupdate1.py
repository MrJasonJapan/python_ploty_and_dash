#######
# This page updates when refreshed.
######
from ast import Div
import dash
import dash_html_components as html
from datetime import datetime

app = dash.Dash()

count = 0


def update_layout():
    global count  # grab the global scopped count variable
    count += 1
    return html.Div([
        html.H1('The time is: ' + str(datetime.now())),
        html.H1('The refresh count: ' + str(count))
    ])


app.layout = update_layout

if __name__ == '__main__':
    app.run_server()
