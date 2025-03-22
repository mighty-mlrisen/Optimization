from dash import html, dcc
from layouts.layout1 import *
from layouts.layout2 import *

layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'border-radius': '8px',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
        'width': '100%',
        'box-sizing': 'border-box',
    },
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(
            style={
                'width': '100%',
                'max-width': '1500px',
                'margin': '0 auto',
                'padding': '0 20px',
                'box-sizing': 'border-box',
            },
            children=[
                dcc.Dropdown(
                    id='task-selector',
                    options=[
                        {'label': 'Градиентный спуск', 'value': 'task1'},
                        {'label': 'Симплекс-метод', 'value': 'task2'},
                    ],
                    value='task1',
                    style={
                        'width': '40%',
                        'margin-bottom': '20px',
                        'margin-left': '20px',
                        'margin-right': '20px',
                    }
                ),
                html.Div(id='page-content')
            ]
        )
    ]
)

