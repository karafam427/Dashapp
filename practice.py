import dash                             # dash is the framework, Dash is the class
import dash_html_components as html     # there are other dash libraries but this is the most basic
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import base64


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Where should you travel?'
    style={
            'textAlign': 'left',
            'color': 'black'
        }),
        
    html.Div(children='''
        A recommendation engine for helping you decide what do with all of your unused PTO.
    ''', style={
        'textAlign': 'left',
        'color': 'grey'',
        ‘background-image’: ‘url(https://images.pexels.com/photos/346885/pexels-photo-346885.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)’,
    }),
    ###how do i add an image?

#free text area
    dcc.Input(
        placeholder='What do you care about in your vacation?'
        type='text'
        value=''
    )
    dcc.Dropdown(
    options=[
        {'label': 'Aberdare National Park', 'value': '???'},
        {'label': 'Abu Simbel', 'value': '???'},
        {'label': 'Adelaide', 'value': '???'}
    ],
    value=['MTL', 'NYC'],
    multi=True,
    placeholder="Are there any places you don't want to go?",
)

if __name__ == '__main__':
    app.run_server(debug=True)
