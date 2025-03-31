from dash.dependencies import Input, Output
from dash import dcc, html, dash_table
import numpy as np
import math
import plotly.graph_objects as go
from methods.gradient import gradient_descent_method
from methods.simplex_method import simplex_method
from methods.genetic_algorithm import genetic_algorithm
from layouts.layout import *
from methods.surface import generate_3d_surface

def functions(function_name):
    s = function_name.lower()
    match s:
        case "rosenbrock":
            return lambda x, y: (1-x)**2 + 100*((y-x**2)**2)
        case "rastrygin":
            return lambda x, y: 20 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))
        case "schwefel":
            return lambda x, y: 418.9829 * 2 - (x * np.sin(np.sqrt(np.abs(x))) + y * np.sin(np.sqrt(np.abs(y))))
        case "himmelblau":
            return lambda x, y: (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def register_callbacks(app):
    # смена страницы задания
    @app.callback(
        Output('page-content', 'children'),
        Input('task-selector', 'value')
    )
    def update_page(selected_task):
        match selected_task:
            case 'task1':
                return layout_task1
            case 'task2':
                return layout_task2
            case 'task3':
                return layout_task3
            case _:
                return html.Div("Задача не найдена")
    
    # метод градиентного спуска
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
        function = lambda x, y: 2 * x**2 + x * y + y**2
        fig = generate_3d_surface(func=function)  

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


        
        fig = generate_3d_surface(func=function, path=result['point_history'])

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

    # симплекс-метод
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
        
        function = lambda x, y: coeffs_f[0] * x**2 + coeffs_f[1] * y**2 + coeffs_f[2] * x * y + coeffs_f[3] * x + coeffs_f[4] * y
        
        coeffs_constraints = [a1, b1, c1, a2, b2, c2]
        coeffs_constraints = [float(coef) if coef is not None else 0.0 for coef in coeffs_constraints]
        
        fig = generate_3d_surface(func=function)
        
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
            
            fig = generate_3d_surface(func=function, point=[result[0]['x'], result[0]['y']])
            
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
    
    # генетический алгоритм
    @app.callback(
        [Output('ga-result-output', 'children'),
         Output('ga-plot', 'figure'),
         Output('ga-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('ga-function', 'value'),
         Input('ga-chroms', 'value'),
         Input('ga-maxiter', 'value'),
         Input('ga-x01', 'value'),
         Input('ga-x02', 'value'),
         Input('ga-y01', 'value'),
         Input('ga-y02', 'value'),
         Input('ga-crossover-prob', 'value'),
         Input('ga-mutation-prob', 'value'),
         Input('ga-mutation-param', 'value'),
         Input('ga-use-cross', 'value'),
         Input('ga-use-mutation', 'value'),
         ]
    )
    
    def run_genetic_algorithm(n_clicks, function, population_size, max_iter, x01, x02, y01, y02, crossover_prob, mutation_prob, mutation_param, use_cross, use_mutation):
        func = functions(function)
        fig = generate_3d_surface(func=func)
        
        bounds = [
            [x01, x02],
            [y01, y02]
        ]
        
        used_methods={
            "crossover": True if use_cross else False,
            "mutation": True if use_mutation else False
        }
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
        
        history, converged, message = genetic_algorithm(
            func, bounds, used_methods, population_size, 
            crossover_prob, mutation_prob, mutation_param, max_iter
            )
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
            ])
            
            fig = generate_3d_surface(func=func, path=path)
            
            table = dash_table.DataTable(
                columns=[
                    {'name': 'Итерация', 'id': 'iteration', 'type': 'numeric'},
                    {'name': 'x', 'id': 'x', 'type': 'numeric', 'format': {'specifier': '.6f'}},
                    {'name': 'y', 'id': 'y', 'type': 'numeric', 'format': {'specifier': '.6f'}},
                    {'name': 'Значение функции', 'id': 'f_value', 'type': 'numeric', 'format': {'specifier': '.6f'}},
                ],
                data=[
                    {
                        "iteration": item["iteration"],
                        "x": item["x"],
                        "y": item["y"],
                        "f_value": item["f_value"]
                    }
                    for item in history
                ],
                style_table={'height': '350px', 'overflowY': 'auto'},
                style_cell={'padding': '10px', 'textAlign': 'center'},
                style_header={'backgroundColor': '#f1f1f1', 'fontWeight': 'bold'}
            )
            return result_text, fig, table
        else:
            return html.Div(message, style={'color': 'red'}), fig, None
        

        
        

