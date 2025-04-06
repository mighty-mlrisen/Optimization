from dash import html, dcc
from layouts.styles import *

layout_task5 = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'border-radius': '8px',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
        'width': '100%',
        'margin': 'auto',
    },
    children=[
        html.Div(
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'space-between',
                'margin-bottom': '30px',
            },
            children=[
                # params
                html.Div(
                    style={
                        'width': '600px',
                        'background-color': '#fff',
                        'padding': '20px',
                        'border-radius': '8px',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                        'margin-right': '20px',
                        'display': 'flex',
                        'flex-direction': 'column'
                    },
                    children=[
                        html.H3("Алгоритм пчёл", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        dcc.Dropdown(
                            id='bee-function',
                            options=[
                                {'label': 'Функция Розенброка', 'value': 'rosenbrock'},
                                {'label': 'Функция Растригина', 'value': 'rastrygin'},
                                {'label': 'Функция Швефеля', 'value': 'schwefel'},
                                {'label': 'Функция Химмельблау', 'value': 'himmelblau'}
                            ],
                            value='rosenbrock',
                            style={
                                'width': '100%',
                                'box-sizing': 'border-box'
                            }
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Кол-во пчел-разведчиков:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-scout', type='number', placeholder='x10', value=300, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Кол-во пчел, отправляемых на лучшие участки:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-best', type='number', placeholder='x20', value=30, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Кол-во пчел, отправляемых на другие выбранные участки:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-selected', type='number', placeholder='x20', value=10, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Кол-во выбранных участков:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-sel-sites', type='number', placeholder='x20', value=15, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Кол-во лучших участков:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-best-sites', type='number', placeholder='x20', value=5, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Интервал области для участка:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-range1', type='number', placeholder='a1', value=100, style=input_style, required=True),
                                dcc.Input(id='bee-range2', type='number', placeholder='a1', value=100, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Интервал по x:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-x01', type='number', placeholder='a1', value=-20, style=input_style, required=True),
                                dcc.Input(id='bee-x02', type='number', placeholder='a1', value=20, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Интервал по y:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-y01', type='number', placeholder='a1', value=-20, style=input_style, required=True),
                                dcc.Input(id='bee-y02', type='number', placeholder='a1', value=20, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Макс. число итераций:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bee-max-iter', type='number', placeholder='x20', value=1000, style=input_style, required=True),
                            ]
                        ),

                        html.Button('Запуск', id='run-button', style=button_style),
                    
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='bee-plot', style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='bee-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='bee-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)