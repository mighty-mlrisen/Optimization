from dash import html, dcc
from layouts.layout1 import *
from layouts.layout2 import *
from layouts.layout3 import *
from layouts.layout4 import *
from layouts.layout5 import *
from layouts.layout6 import *
from layouts.layout7 import *
from layouts.layout8 import *

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
                        {'label': 'Генетический алгоритм', 'value': 'task3'},
                        {'label': 'Алгоритм роя частиц', 'value': 'task4'},
                        {'label': 'Алгоритм пчёл', 'value': 'task5'},
                        {'label': 'Алгоритм искусственной имунной сети', 'value': 'task6'},
                        {'label': 'Алгоритм бактериальной оптимизации', 'value': 'task7'},
                        {'label': 'Гибридный алгоритм', 'value': 'task8'},
                    ],
                    value='task1',
                    style={
                        'width': '50%',
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

