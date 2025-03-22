from dash import html, dcc

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Dropdown(
            id='task-selector',
            options=[
                {'label': 'Задача 1: Градиентный спуск', 'value': 'task1'},
                {'label': 'Задача 2: Другая задача', 'value': 'task2'},
            ],
            value='task1',
            style={'width': '100%', 'margin-bottom': '20px'}
        ),
        html.Div(id='page-content')
    ])
])

layout_task1 = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'border-radius': '8px',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
        'width': '400px',
        'margin': 'auto',
        'height' : '600px'
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
            'border-radius': '4px'
        }),

        html.Label("x2:", style={'margin-bottom': '5px'}),
        dcc.Input(id='initial-point-x2', type='number', placeholder='x2', value=2, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("Шаг:", style={'margin-bottom': '5px'}),
        dcc.Input(id='step', type='number', placeholder='Step', value=0.1, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon', type='number', placeholder='Epsilon', value=0.0001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon1:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon1', type='number', placeholder='Epsilon1', value=0.00001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon2:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon2', type='number', placeholder='Epsilon2', value=0.00001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("Максимальное количество итераций:", style={'margin-bottom': '5px'}),
        dcc.Input(id='max-iterations', type='number', placeholder='Max iterations', value=100, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '20px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
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


        dcc.Graph(id='surface-plot', style={'width': '1500px', 'height': '500px', 'margin-top': '30px'}),


        html.Div(id='result-output', style={
            'margin-top': '30px',
            'padding': '20px',
            'background-color': '#fff',
            'border': '1px solid #ccc',
            'border-radius': '8px',
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
            'width': '1200px',
            'max-width': '1200px',
            'text-align': 'left',
            'font-size': '16px',
        }),

        html.Div(id='iterations-table', style={
            'margin-top': '30px',
            'padding': '20px',
            'background-color': '#fff',
            'border': '1px solid #ccc',
            'border-radius': '8px',
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
            'width': '1000px',
            'max-width': '1200px',
            'text-align': 'left',
        }),

    ]
)

layout_task2 = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'padding': '20px',
        'background-color': '#f4f4f4',
        'border-radius': '8px',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
        'width': '400px',
        'margin': 'auto',
        'height' : '600px'
    },
    children=[
        html.H3("Симплекс-метод", style={
            'margin-bottom': '20px',
            'color': '#333'
        }),

        html.Label("x1:", style={'margin-bottom': '5px'}),
        dcc.Input(id='initial-point-x1', type='number', placeholder='x1', value=2, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("x2:", style={'margin-bottom': '5px'}),
        dcc.Input(id='initial-point-x2', type='number', placeholder='x2', value=2, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("Шаг:", style={'margin-bottom': '5px'}),
        dcc.Input(id='step', type='number', placeholder='Step', value=0.1, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon', type='number', placeholder='Epsilon', value=0.0001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon1:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon1', type='number', placeholder='Epsilon1', value=0.00001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("epsilon2:", style={'margin-bottom': '5px'}),
        dcc.Input(id='epsilon2', type='number', placeholder='Epsilon2', value=0.00001, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '15px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
        }),

        html.Label("Максимальное количество итераций:", style={'margin-bottom': '5px'}),
        dcc.Input(id='max-iterations', type='number', placeholder='Max iterations', value=100, style={
            'width': '100%',
            'padding': '8px',
            'margin-bottom': '20px',
            'border': '1px solid #ccc',
            'border-radius': '4px'
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


        dcc.Graph(id='surface-plot', style={'width': '1500px', 'height': '500px', 'margin-top': '30px'}),


        html.Div(id='result-output', style={
            'margin-top': '30px',
            'padding': '20px',
            'background-color': '#fff',
            'border': '1px solid #ccc',
            'border-radius': '8px',
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
            'width': '1200px',
            'max-width': '1200px',
            'text-align': 'left',
            'font-size': '16px',
        }),

        html.Div(id='iterations-table', style={
            'margin-top': '30px',
            'padding': '20px',
            'background-color': '#fff',
            'border': '1px solid #ccc',
            'border-radius': '8px',
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
            'width': '1000px',
            'max-width': '1200px',
            'text-align': 'left',
        }),

    ]
)

