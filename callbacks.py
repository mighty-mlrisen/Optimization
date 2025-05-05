from dash.dependencies import Input, Output
from dash import dcc, html, dash_table
import numpy as np
import math
import plotly.graph_objects as go
from methods.gradient import gradient_descent_method
from methods.simplex_method import simplex_method
from methods.genetic_algorithm import genetic_algorithm
from methods.particle_swarm import particle_swarm
from methods.bee_algorithm import bee_algorithm
from methods.ais_algorithm import ais_optimize
from methods.bfo import bacterial_foraging_optimization
from layouts.layout import *
from methods.surface import generate_3d_surface
from dash.exceptions import PreventUpdate

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
        case "negative_sphere_function":
            return lambda x, y: -(x**2 + y**2)

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
            case 'task4':
                return layout_task4
            case 'task5':
                return layout_task5
            case 'task6':
                return layout_task6
            case 'task7':
                return layout_task7
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
        
        last_item = history[-1]
        x = last_item['x']
        y = last_item['y']
        func_value = last_item['f_value'] 
        iteration = last_item['iteration']
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f'Число итераций: {iteration}', style={'margin': '5px 0'}),
                html.P(f'Точка минимума: ({x:.6f}, {y:.6f})', style={'margin': '5px 0'}),  
                html.P(f'Значение функции: {func_value:.6f}', style={'margin': '5px 0', 'font-weight': 'bold'}),
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
        

    # алгоритм роя частиц
    @app.callback(
        [Output('ps-result-output', 'children'),
         Output('ps-plot', 'figure'),
         Output('ps-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('ps-function', 'value'),
         Input('ps-maxiter', 'value'),
         Input('ps-swarm-size', 'value'),
         Input('ps-x01', 'value'),
         Input('ps-x02', 'value'),
         Input('ps-y01', 'value'),
         Input('ps-y02', 'value'),
         Input('ps-current-velocity-ratio', 'value'),
         Input('ps-local-velocity-ratio', 'value'),
         Input('ps-global-velocity-ratio', 'value'), 
         Input('ps-penalty-ratio', 'value'),
         Input('ps-eps', 'value')
         ]
    )
    
    def run_particle_swarm(n_clicks, function, iter_count, swarm_size, x01, x02, y01, y02, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio, penalty_ratio,eps):
        func = functions(function)
        fig = generate_3d_surface(func=func)

        if current_velocity_ratio <= 0 or current_velocity_ratio >= 1:
            raise PreventUpdate 
        
        bounds = [
            [x01, y01],
            [x02, y02]
        ]
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
        
        wrapped_func = lambda pos: func(*pos)
        
        history, converged, message = particle_swarm(
            wrapped_func, iter_count, swarm_size, bounds, 
            current_velocity_ratio, local_velocity_ratio, global_velocity_ratio, penalty_ratio, eps
            )
        
        last_item = history[-1]
        x = last_item['x']
        y = last_item['y']
        func_value = last_item['f_value'] 
        iteration = last_item['iteration']
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f'Число итераций: {iteration}', style={'margin': '5px 0'}),
                html.P(f'Точка минимума: ({x:.6f}, {y:.6f})', style={'margin': '5px 0'}),  
                html.P(f'Значение функции: {func_value:.6f}', style={'margin': '5px 0', 'font-weight': 'bold'}),
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
    



    # Алгоритм пчёл
    @app.callback(
        [Output('bee-result-output', 'children'),
         Output('bee-plot', 'figure'),
         Output('bee-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('bee-function', 'value'),
         Input('bee-scout', 'value'),
         Input('bee-selected', 'value'),
         Input('bee-best', 'value'),
         Input('bee-sel-sites', 'value'),
         Input('bee-best-sites', 'value'),
         Input('bee-range1', 'value'),
         Input('bee-range2', 'value'),
         Input('bee-x01', 'value'),
         Input('bee-x02', 'value'), 
         Input('bee-y01', 'value'),
         Input('bee-y02', 'value'),
         Input('bee-max-iter', 'value')
         ]
    )

    def run_bee_algorithm(n_clicks, function, scout_bee_count, selected_bee_count,best_bee_count,sel_sites_count,best_sites_count,range1,range2, x01,x02,y01,y02,max_iter):
        func = functions(function)
        fig = generate_3d_surface(func=func)
        
        range_list = [range1,range2]

        minval = [x01,y01]
        maxval = [x02,y02]   
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
        
        wrapped_func = lambda pos: -func(*pos)
        
        history, converged, message = bee_algorithm(
            wrapped_func, scout_bee_count,selected_bee_count,best_bee_count,sel_sites_count,
            best_sites_count,range_list,minval,maxval,max_iter
            )
        
        last_item = history[-1]
        x = last_item['x']
        y = last_item['y']
        func_value = -last_item['f_value'] 
        iteration = last_item['iteration']
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f'Число итераций: {iteration}', style={'margin': '5px 0'}),
                html.P(f'Точка минимума: ({x:.6f}, {y:.6f})', style={'margin': '5px 0'}),  
                html.P(f'Значение функции: {func_value:.6f}', style={'margin': '5px 0', 'font-weight': 'bold'}),
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
                        "f_value": -item["f_value"]
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
        

    # Алгоритм искусственной имунной сети
    @app.callback(
        [Output('ais-result-output', 'children'),
         Output('ais-plot', 'figure'),
         Output('ais-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('ais-function', 'value'),
         Input('ais-pop-size', 'value'),
         Input('ais-n-b', 'value'),
         Input('ais-n-c', 'value'),
         Input('ais-n-d', 'value'),
         Input('ais-alpha', 'value'),
         Input('ais-range1', 'value'),
         Input('ais-range2', 'value'),
         Input('ais-max-iter', 'value')
         ]
    )
    
    def run_ais_algorithm(n_clicks, func, pop_size, n_b, n_c, n_d, alpha, range1, range2, generations):
        func = functions(func)
        funct = lambda pos: func(pos[0], pos[1])
        
        fig = generate_3d_surface(func=func)
        bounds = [range1, range2]
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
        
        history, converged, message = ais_optimize(
            funct,
            dim=2,
            pop_size=pop_size,
            n_b=n_b,
            n_c=n_c,
            n_d=n_d,
            alpha=alpha,
            bounds=bounds,
            generations=generations,
            verbose=True
        )
        
        last_item = history[-1]
        x = last_item['x']
        y = last_item['y']
        func_value = last_item['f_value'] 
        iteration = last_item['iteration']
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f'Число итераций: {iteration}', style={'margin': '5px 0'}),
                html.P(f'Точка минимума: ({x:.6f}, {y:.6f})', style={'margin': '5px 0'}),  
                html.P(f'Значение функции: {func_value:.6f}', style={'margin': '5px 0', 'font-weight': 'bold'}),
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
            return html.Div(result_text, style={'color': 'red'}), fig, None
        


    # Бактериальный алгоритм 
    @app.callback(
        [Output('bfo-result-output', 'children'),
         Output('bfo-plot', 'figure'),
         Output('bfo-table', 'children')],
        [Input('run-button', 'n_clicks')],
        [Input('bfo-function', 'value'),
         Input('bfo-pop-size', 'value'),
         Input('bfo-range1', 'value'),
         Input('bfo-range2', 'value'),
         Input('bfo-t-chem', 'value'),
         Input('bfo-t-rep', 'value'),
         Input('bfo-t-elim', 'value'),
         Input('bfo-step-size', 'value'),
         Input('bfo-elim-prob', 'value'),
         Input('bfo-elim-num', 'value')
         ]
    )
    def run_bfo_algorithm(n_clicks, func, pop_size,range1, range2, t_chemotaxis, t_reproduction, t_elimination, step_size, elimination_prob, elimination_num):
        
        func = functions(func)

        wrapped_func = lambda point: func(point[0], point[1])
        
        fig = generate_3d_surface(func=func)
        bounds = [range1, range2]
        
        if n_clicks is None or n_clicks == 0:
            return "", fig, None 
        
        history, converged, message = bacterial_foraging_optimization(
            wrapped_func,
            pop_size,
            bounds,
            t_chemotaxis,
            t_reproduction,
            t_elimination,
            step_size,
            elimination_prob,
            elimination_num
        )
        
        last_item = history[-1]
        x = last_item['x']
        y = last_item['y']
        func_value = last_item['f_value'] 
        iteration = last_item['iteration']
        
        if converged == True:
            path = [(item['x'], item['y']) for item in history]
            
            result_text = html.Div([
                html.P(message, style={'margin': '5px 0', 'font-weight': 'bold'}),
                html.P(f'Число итераций: {iteration}', style={'margin': '5px 0'}),
                html.P(f'Точка максимума: ({x:.6f}, {y:.6f})', style={'margin': '5px 0'}),  
                html.P(f'Значение функции: {func_value:.6f}', style={'margin': '5px 0', 'font-weight': 'bold'}),
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
            return html.Div(result_text, style={'color': 'red'}), fig, None   
        

        
        

