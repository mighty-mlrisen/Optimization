from dash.dependencies import Input, Output
from dash import dcc, html, dash_table
import numpy as np
import math
import plotly.graph_objects as go
from methods.gradient import gradient_descent_method, gradient_generate_3d_surface
from methods.simplex_method import simplex_method, simplex_generate_3d_surface
from layouts.layout import *

def register_callbacks(app):
    @app.callback(
        Output('page-content', 'children'),
        Input('task-selector', 'value')
    )
    def update_page(selected_task):
        if selected_task == 'task1':
            return layout_task1
        elif selected_task == 'task2':
            return layout_task2
        else:
            return html.Div("Задача не найдена")
    
    @app.callback(
        [Output('gradient-result-output', 'children'),
         Output('gradient-plot', 'figure'),
         Output('gradient-table', 'children')],
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
        fig = gradient_generate_3d_surface()  

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


        
        fig = gradient_generate_3d_surface(path=result['point_history'])

        table = dash_table.DataTable(
            columns=[
                {'name': 'Итерация', 'id': 'iteration'},
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


    @app.callback(
        [Output('simplex-result-output', 'children'),
         Output('simplex-plot', 'figure'),
         Output('simplex-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('simplex-x10', 'value'),
         Input('simplex-x20', 'value'),
         Input('simplex-a1', 'value'),
         Input('simplex-a2', 'value'),
         Input('simplex-a3', 'value'),
         Input('simplex-a4', 'value'),
         Input('simplex-a5', 'value'),
         Input('simplex-cons-a1', 'value'),
         Input('simplex-cons-b1', 'value'),
         Input('simplex-cons-c1', 'value'),
         Input('simplex-cons-a2', 'value'),
         Input('simplex-cons-b2', 'value'),
         Input('simplex-cons-c2', 'value'),
         Input('simplex-minmax', 'value'),
         ]
    )
    
    def run_simplex_method(n_clicks, x1, x2, coef1, coef2, coef3, coef4, coef5, a1, b1, c1, a2, b2, c2, minmax):        
        initial_x = [x1, x2]
        
        coeffs_f = [coef1, coef2, coef3, coef4, coef5]
        coeffs_f = [float(coef) if coef is not None else 1.0 for coef in coeffs_f]
        
        coeffs_constraints = [a1, b1, c1, a2, b2, c2]
        coeffs_constraints = [float(coef) if coef is not None else 0.0 for coef in coeffs_constraints]
        
        fig = simplex_generate_3d_surface(coeffs_f)
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
    
        result, success, message = simplex_method(initial_x, coeffs_f, coeffs_constraints, minmax)
        
        if success == True:
            result_text = html.Div([
                html.P(message, 
                    style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f"Значение функции в точке {"минимума" if minmax == "minimize" else "максимума"} {round(result[0]['f_value'], 10)}", style={'margin': '5px 0'}),
                html.P(f"Количество итераций: {result[0]['iteration']}", style={'margin': '5px 0'}),
            ])
            
            fig = simplex_generate_3d_surface(coeffs_f, point=[result[0]['x'], result[0]['y']])
            
            table_data = [
                {
                    "simplex-iterations": result[0]['iteration'],
                    "simplex-x": round(result[0]['x'], 6),
                    "simplex-y": round(result[0]['y'], 6),
                    "simplex-f_value": round(result[0]['f_value'], 6)
                }
            ]
            
            table = dash_table.DataTable(
                columns=[
                    {'name': 'Итерация', 'id': 'simplex-iterations'},
                    {'name': 'x', 'id': 'simplex-x'},
                    {'name': 'y', 'id': 'simplex-y'},
                    {'name': 'f', 'id': 'simplex-f_value'},
                ],
                data = table_data,
                style_table={'height': '90px', 'overflowY': 'auto'},
                style_cell={'padding': '10px', 'textAlign': 'center'},
                style_header={'backgroundColor': '#f1f1f1', 'fontWeight': 'bold'}
            )        
            return result_text, fig, table
        else:
            return html.Div(message, style={'color': 'red'}), fig, None