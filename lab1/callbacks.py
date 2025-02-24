from dash.dependencies import Input, Output
from dash import dcc, html, dash_table
import numpy as np
import math
import plotly.graph_objects as go
from gradient import gradient_descent_method, generate_3d_surface

def register_callbacks(app):
    @app.callback(
        [Output('result-output', 'children'),
         Output('surface-plot', 'figure'),
         Output('iterations-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('initial-point-x1', 'value'),
         Input('initial-point-x2', 'value'),
         Input('step', 'value'),
         Input('epsilon', 'value'),
         Input('epsilon1', 'value'),
         Input('epsilon2', 'value'),
         Input('max-iterations', 'value')]
    )
    def run_gradient_descent(n_clicks, x1, x2, step, epsilon, epsilon1, epsilon2, max_iterations):
        fig = generate_3d_surface()  

        if n_clicks is None or n_clicks == 0:
            return "", fig, None  

        initial_point = [x1, x2]
        step = float(step)
        epsilon = float(epsilon1)
        epsilon1 = float(epsilon1)
        epsilon2 = float(epsilon2)
        max_iterations = int(max_iterations)
        
        result = gradient_descent_method(initial_point, step, epsilon, epsilon1, epsilon2, max_iterations)
        
        result_text = html.Div([
            html.P(f"Минимум найден в точке: ({result['min_point'][0]:.6f}, {result['min_point'][1]:.6f})", 
                style={'margin': '5px 0', 'font-weight': 'bold'}),
            html.P(f"Значение функции в точке минимуме: {round(result['min_value'], 10)}", style={'margin': '5px 0'}),
            html.P(f"Количество итераций: {result['iterations']}", style={'margin': '5px 0'}),
            html.P(f"Условие остановки: {result['condition']}", style={'margin': '5px 0'}),
        ])


        
        fig = generate_3d_surface(path=result['point_history'])

        table = dash_table.DataTable(
            columns=[
                {'name': 'k', 'id': 'iteration'},
                {'name': 'x1', 'id': 'x1'},
                {'name': 'x2', 'id': 'x2'},
                {'name': 'Норма', 'id': 'norm'},
            ],
            data = [
                    {
                        "iteration":i,
                        "x1": round(point[0], 6),
                        "x2":round(point[1], 6),
                        "norm": round(norm, 6)
                    }
                    for i, (point, norm) in enumerate(zip(result["point_history"], result["norm_history"]))
                    
            ],
            style_table={'height': '350px', 'overflowY': 'auto'},
            style_cell={'padding': '10px', 'textAlign': 'center'},
            style_header={'backgroundColor': '#f1f1f1', 'fontWeight': 'bold'}
        )
        
        return result_text, fig, table
