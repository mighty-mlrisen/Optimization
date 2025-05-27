from dash import html, dcc
from layouts.styles import *

layout_task7 = html.Div(
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
                        html.H3("Алгоритм бактериальной оптимизации", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        dcc.Dropdown(
                            id='bfo-function',
                            options=[
                                {'label': 'Функция Розенброка', 'value': 'rosenbrock'},
                                {'label': 'Функция Растригина', 'value': 'rastrygin'},
                                {'label': 'Функция Швефеля', 'value': 'schwefel'},
                                {'label': 'Функция Химмельблау', 'value': 'himmelblau'},
                                {'label': 'Обратная сферическая функция', 'value': 'negative_sphere_function'}
                            ],
                            value='negative_sphere_function',
                            style={
                                'width': '100%',
                                'box-sizing': 'border-box'
                            }
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Размер популяции:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-pop-size', type='number', placeholder='10', value=50, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Границы:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-range1', type='number', placeholder='-3', value=-5, style=input_style, required=True),
                                dcc.Input(id='bfo-range2', type='number', placeholder='3', value=5, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число шагов хемотаксиса:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-t-chem', type='number', placeholder='10', value=30, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число шагов репродукции:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-t-rep', type='number', placeholder='5', value=10, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число шагов ликвидации:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-t-elim', type='number', placeholder='5', value=10, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Начальный размер шага хемотаксиса:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-step-size', type='number', placeholder='0.5', value=0.1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Вероятность ликвидации бактерии:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-elim-prob', type='number', placeholder='100', value=0.1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Число уничтожаемых бактерий:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='bfo-elim-num', type='number', placeholder='100', value=5, style=input_style, required=True),
                            ]
                        ),

                        html.Button('Запуск', id='run-button', style=button_style),
                    
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='bfo-plot', style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='bfo-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='bfo-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)