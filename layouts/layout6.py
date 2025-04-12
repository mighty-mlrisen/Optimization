from dash import html, dcc
from layouts.styles import *

layout_task6 = html.Div(
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
                        html.H3("Алгоритм искусственной имунной сети", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        dcc.Dropdown(
                            id='ais-function',
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
                                html.Label("Размер популяции:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-pop-size', type='number', placeholder='50', value=50, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число антител с наилучшей афинностью:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-n-b', type='number', placeholder='10', value=10, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число клонов, создаваемых для каждого лучшего антитела:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-n-c', type='number', placeholder='5', value=5, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число клонов, оставляемых после мутации:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-n-d', type='number', placeholder='5', value=5, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Коэффициент мутации:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-alpha', type='number', placeholder='0.5', value=0.5, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Границы:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-range1', type='number', placeholder='-3', value=-3, style=input_style, required=True),
                                dcc.Input(id='ais-range2', type='number', placeholder='3', value=3, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Макс. число поколений:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='ais-max-iter', type='number', placeholder='100', value=100, style=input_style, required=True),
                            ]
                        ),

                        html.Button('Запуск', id='run-button', style=button_style),
                    
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='ais-plot', style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='ais-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='ais-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)