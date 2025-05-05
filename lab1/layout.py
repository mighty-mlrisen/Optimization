from dash import html, dcc

# Layout для главной страницы
index_layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'justify-content': 'center',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'min-height': '100vh',
    },
    children=[
        html.H1(
            "Главная страница",
            style={
                'margin-bottom': '20px',
                'color': '#333',
                'font-size': '32px',
                'font-weight': 'bold',
            }
        ),
        html.Div(
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'gap': '15px',
                'align-items': 'center',
            },
            children=[
                dcc.Link(
                    'Градиентный спуск',
                    href='/gradient',
                    style={
                        'font-size': '20px',
                        'color': '#007BFF',
                        'text-decoration': 'none',
                        'padding': '10px 20px',
                        'border': '1px solid #007BFF',
                        'border-radius': '5px',
                        'transition': 'background-color 0.3s ease',
                    }
                ),
                dcc.Link(
                    'Другая задача',
                    href='/other-task',
                    style={
                        'font-size': '20px',
                        'color': '#007BFF',
                        'text-decoration': 'none',
                        'padding': '10px 20px',
                        'border': '1px solid #007BFF',
                        'border-radius': '5px',
                        'transition': 'background-color 0.3s ease',
                    }
                ),
            ]
        ),
    ]
)

# Layout для страницы градиентного спуска
gradienslayout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'min-height': '100vh',
    },
    children=[
        html.H3(
            "Метод градиентного спуска",
            style={
                'margin-bottom': '20px',
                'color': '#333',
                'font-size': '24px',
                'font-weight': 'bold',
            }
        ),

        html.Div(
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'gap': '20px',
                'width': '100%',
                'max-width': '1500px',
                'margin-bottom': '30px',
            },
            children=[
                html.Div(
                    style={
                        'flex': '0 0 400px',
                        'background-color': '#fff',
                        'padding': '20px',
                        'border-radius': '8px',
                        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                    },
                    children=[
                        html.Label("x1:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='initial-point-x1',
                            type='number',
                            placeholder='x1',
                            value=2,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("x2:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='initial-point-x2',
                            type='number',
                            placeholder='x2',
                            value=2,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("Шаг:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='step',
                            type='number',
                            placeholder='Step',
                            value=0.1,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("epsilon:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='epsilon',
                            type='number',
                            placeholder='Epsilon',
                            value=0.0001,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("epsilon1:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='epsilon1',
                            type='number',
                            placeholder='Epsilon1',
                            value=0.00001,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("epsilon2:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='epsilon2',
                            type='number',
                            placeholder='Epsilon2',
                            value=0.00001,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '15px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Label("Максимальное количество итераций:", style={'margin-bottom': '5px'}),
                        dcc.Input(
                            id='max-iterations',
                            type='number',
                            placeholder='Max iterations',
                            value=100,
                            style={
                                'width': '100%',
                                'padding': '8px',
                                'margin-bottom': '20px',
                                'border': '1px solid #ccc',
                                'border-radius': '4px',
                            }
                        ),

                        html.Button(
                            'Запуск',
                            id='run-button',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'background-color': '#000000',
                                'color': 'white',
                                'border': 'none',
                                'border-radius': '4px',
                                'cursor': 'pointer',
                                'font-size': '16px',
                                'transition': 'background-color 0.3s ease',
                            }
                        ),
                    ]
                ),

                dcc.Graph(
                    id='surface-plot',
                    style={
                        'flex': '1',
                        'height': '500px',
                        'border-radius': '8px',
                        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                    }
                ),
            ]
        ),

        html.Div(
            id='result-output',
            style={
                'width': '100%',
                'max-width': '1500px',
                'background-color': '#fff',
                'padding': '20px',
                'border-radius': '8px',
                'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                'text-align': 'left',
                'font-size': '16px',
            }
        ),

        html.Div(
            id='iterations-table',
            style={
                'width': '100%',
                'max-width': '1500px',
                'background-color': '#fff',
                'padding': '20px',
                'border-radius': '8px',
                'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                'margin-bottom': '30px',
            }
        ),
    ]
)