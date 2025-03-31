
from scipy.optimize import minimize, linprog
import numpy as np

def f(x, coeffs):
    x1, x2 = x[0], x[1]
    return coeffs[0] * x1 ** 2 + coeffs[1] * x2 ** 2 + coeffs[2] * x1 * x2 + coeffs[3] * x1 + coeffs[4] * x2

def create_constraints(coeffs_con):
    constraints_list = []
    for i in range(0, len(coeffs_con), 3):
        a, b, c = coeffs_con[i], coeffs_con[i + 1], coeffs_con[i + 2]
        
        constraints_list.append({
            'type': 'ineq',
            'fun': lambda x, a=a, b=b, c=c: c - (a * x[0] + b * x[1])
        })

    constraints_list.append({
        'type': 'ineq',
        'fun': lambda x: x[0]
    })
    constraints_list.append({
        'type': 'ineq',
        'fun': lambda x: x[1]
    })

    return constraints_list

def simplex_method(x0, coeffs_f, coeffs_con, opt_type):
    
    if opt_type == "minimize":
        result = minimize(lambda x, coeffs: f(x, coeffs), x0,
                         args=coeffs_f, constraints=create_constraints(coeffs_con),
                         options={'maxiter': 1000, 'ftol': 1e-8})
        f_value = result.fun
    elif opt_type == "maximize":
        result = minimize(lambda x, coeffs: -f(x, coeffs), x0,
                         args=coeffs_f, constraints=create_constraints(coeffs_con),
                         options={'maxiter': 1000, 'ftol': 1e-8})
        f_value = -result.fun
    
    if result.success:
        status = True
        function_type = "минимум" if opt_type == "minimize" else "максимум"
        message = f"{function_type.capitalize()} функции найден в точке ({result.x[1]}, {result.x[0]})"
        result_info = [{
            'iteration': result.nit,
            'x': result.x[0],
            'y': result.x[1],
            'f_value': f_value
        }]
    else:
        status = False
        message = f"Оптимизация не завершена успешно: {result.message}"
        function_type = "минимум" if opt_type == "minimize" else "максимум"
        result_info = [{
            'iteration': "Final",
            'x': result.x[0],
            'y': result.x[1],
            'f_value': f_value
        }]

    return result_info, status, message