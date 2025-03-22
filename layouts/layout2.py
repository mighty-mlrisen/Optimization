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
                                html.Label("x₁₀:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-x10', type='number', placeholder='x10', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("x₂₀:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-x20', type='number', placeholder='x20', value=1, style=input_style, required=True),
                            ]
                        ),
                        
                        html.Label("Коэффициенты целевой функции", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("f(x) = a₁x₁² + a₂x₂² + a₃x₁x₂ + a₄x₁ + a₅x₂:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₁:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a1', type='number', placeholder='a1', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₂:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a2', type='number', placeholder='a2', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₃:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a3', type='number', placeholder='a3', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₄:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a4', type='number', placeholder='a4', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₅:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-a5', type='number', placeholder='a5', value=1, style=input_style, required=True),
                            ]
                        ),

                        html.Label("Условное ограничение 1", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("a₁x + b₁x <= c₁:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₁:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-a1', type='number', placeholder='a', value=0, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("b₁:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-b1', type='number', placeholder='b', value=0, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("c₁:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-c1', type='number', placeholder='c', value=0, style=input_style, required=True),
                            ]
                        ),

                        html.Label("Условное ограничение 1", style={'margin-bottom': '5px', 'font-size': '18px'}),
                        html.Label("a₂x + bx₂ <= c₂:", style={'margin-bottom': '5px', 'font-size': '18px'}),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("a₂:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-a2', type='number', placeholder='a', value=0, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("b₂:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-b2', type='number', placeholder='b', value=0, style=input_style, required=True),
                            ]
                        ),

                        html.Div(
                            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '5px'},
                            children=[
                                html.Label("c₂:", style={'margin-right': '10px', 'width': '30px'}),
                                dcc.Input(id='simplex-cons-c2', type='number', placeholder='c', value=0, style=input_style, required=True),
                            ]
                        ),
                        
                        dcc.Dropdown(
                            id='simplex-minmax',
                            options=[
                                {'label': 'Максимум', 'value': 'maximize'},
                                {'label': 'Минимум', 'value': 'minimize'},
                            ],
                            value='minimize',
                            style={
                                'width': '100%',
                                'box-sizing': 'border-box'
                            }
                        ),
                        html.Button('Запуск', id='run-button', style=button_style),
                    ]
                ),

                # graph
                html.Div(
                    style=graph_style,
                    children=[
                        dcc.Graph(id='simplex-plot', style={'width': '100%', 'height': '100%'}),
                    ]
                ),
            ]
        ),

        # bottom
        html.Div(
            style=bottom_style,
            children=[
                html.Div(id='simplex-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='simplex-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)