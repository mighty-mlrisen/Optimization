from dash import html, dcc
from layouts.styles import *

layout_task8 = html.Div(
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
                        html.H3("Гибридный алгоритм", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        dcc.Dropdown(
                            id='gib-function',
                            options=[
                                {'label': 'Функция Розенброка', 'value': 'rosenbrock'},
                                {'label': 'Функция Растригина', 'value': 'rastrygin'},
                                {'label': 'Функция Швефеля', 'value': 'schwefel'},
                                {'label': 'Функция Химмельблау', 'value': 'himmelblau'},
                                {'label': 'Функция Сферы', 'value': 'sphere'}
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
                                html.Label("Количество хромосом:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ga-size', type='number', placeholder='x10', value=100, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Макс. итераций для генетического:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ga-maxiter', type='number', placeholder='x20', value=100, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Интервал поиска по x:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-x01', type='number', placeholder='a1', value=-3, style=input_style, required=True),
                                dcc.Input(id='gib-x02', type='number', placeholder='a1', value=3, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Интервал поиска по y:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-y01', type='number', placeholder='a1', value=-3, style=input_style, required=True),
                                dcc.Input(id='gib-y02', type='number', placeholder='a1', value=3, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Вероятность скрещивания:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ga-crossover-prob', type='number', placeholder='a3', value=0.7, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Вероятность мутации:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ga-mutation-prob', type='number', placeholder='a4', value=0.1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Параметр мутации:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ga-mutation-param', type='number', placeholder='a5', value=3, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Размер роя:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ps-size', type='number', placeholder='x20', value=70, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Макс. итераций для роя частиц:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ps-maxiter', type='number', placeholder='x10', value=100, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Коэффициент k (0,1):", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(
                                    id='gib-ps-current-velocity-ratio',
                                    type='number',
                                    placeholder='a3',
                                    value=0.5,
                                    style=input_style,
                                    required=True,
                                    min=0,  # Минимальное значение
                                    max=1,  # Максимальное значение
                                 
                                ),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Локальный коэффициент скорости:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ps-local-velocity-ratio', type='number', placeholder='a4', value=2, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Глобальный коэффициент скорости:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ps-global-velocity-ratio', type='number', placeholder='a5', value=5, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("Коэффициент штрафа:", style={'margin': '10px', 'margin-left': '0px'}),
                                dcc.Input(id='gib-ps-penalty-ratio', type='number', placeholder='a5', value=10000, style=input_style, required=True),
                            ]
                        ),

                        html.Button('Запуск', id='run-button', style=button_style),
                    
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='gib-plot', style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='gib-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='gib-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)