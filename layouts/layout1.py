from dash import html, dcc

layout_task1 = html.Div(
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
                    },
                    children=[
                        html.H3("Метод градиентного спуска", style={
                            'margin-bottom': '20px',
                            'color': '#333'
                        }),

                        html.Label("x1:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='initial-point-x1', type='number', placeholder='x1', value=2, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("x2:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='initial-point-x2', type='number', placeholder='x2', value=2, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("Шаг:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='step', type='number', placeholder='Step', value=0.1, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("epsilon:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='epsilon', type='number', placeholder='Epsilon', value=0.0001, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("epsilon1:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='epsilon1', type='number', placeholder='Epsilon1', value=0.00001, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("epsilon2:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='epsilon2', type='number', placeholder='Epsilon2', value=0.00001, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '15px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Label("Максимальное количество итераций:", style={'margin-bottom': '5px'}),
                        dcc.Input(id='max-iterations', type='number', placeholder='Max iterations', value=100, style={
                            'width': '100%',
                            'padding': '8px',
                            'margin-bottom': '20px',
                            'border': '1px solid #ccc',
                            'border-radius': '4px',
                            'box-sizing': 'border-box'
                        }),

                        html.Button('Запуск', id='run-button', style={
                            'width': '100%',
                            'padding': '10px',
                            'background-color': '#000000',
                            'color': 'white',
                            'border': 'none',
                            'border-radius': '4px',
                            'cursor': 'pointer',
                            'font-size': '16px',
                            'transition': 'background-color 0.3s ease'
                        }),
                    ]
                ),
                
                # graph
                html.Div(
                    style={
                        'flex': '1',
                        'background-color': '#fff',
                        'padding': '20px',
                        'border-radius': '8px',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                    },
                    children=[
                        dcc.Graph(id='gradient-plot', style={'width': '100%', 'height': '500px'}),
                    ]
                ),
            ]
        ),
        
        # bottom
        html.Div(
            style={
                'width': '100%',
                'background-color': '#fff',
                'padding': '20px',
                'border-radius': '8px',
                'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                'box-sizing': 'border-box'
            },
            children=[
                html.Div(id='gradient-result-output', style={
                    'margin-bottom': '20px',
                    'font-size': '16px',
                }),
                html.Div(id='gradient-table', style={
                    'width': '100%',
                    'overflowX': 'auto',
                }),
            ]
        ),
    ]
)