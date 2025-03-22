from dash import html, dcc
from layouts.styles import *

layout_task2 = html.Div(
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
                        'width': '400px',
                        'background-color': '#fff',
                        'padding': '20px',
                        'border-radius': '8px',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                        'margin-right': '20px',
                        'display': 'flex',
                        'flex-direction': 'column'
                    },
                    children=[
                        html.H3("Симплекс-метод", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("x10:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-x10', type='number', placeholder='x10', value=1, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("x20:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-x20', type='number', placeholder='x20', value=1, style=input_style),
                            ]
                        ),
                        
                        html.Label("Коэффициенты целевой функции", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("f(x) = a1x1^2 + a2x2^2 + a3x1x2 + a4x1 + a5x2:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a1:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a1', type='number', placeholder='a1', value=1, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a2:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a2', type='number', placeholder='a2', value=1, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a3:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a3', type='number', placeholder='a3', value=1, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a4:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a4', type='number', placeholder='a4', value=1, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a5:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a5', type='number', placeholder='a5', value=1, style=input_style),
                            ]
                        ),

                        html.Label("Условное ограничение 1", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("ax1 + bx2 <= c1:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a1:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-a1', type='number', placeholder='a', value=0, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("b1:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-b1', type='number', placeholder='b', value=0, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("c1:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-c1', type='number', placeholder='c', value=0, style=input_style),
                            ]
                        ),

                        html.Label("Условное ограничение 1", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("ax1 + bx2 <= c1:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a2:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-a2', type='number', placeholder='a', value=0, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("b2:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-b2', type='number', placeholder='b', value=0, style=input_style),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("c2:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-c2', type='number', placeholder='c', value=0, style=input_style),
                            ]
                        ),

                        html.Button('Запуск', id='run-button', style=button_style),
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='surface-plot', style={'width': '100%', 'height': '500px'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='iterations-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)