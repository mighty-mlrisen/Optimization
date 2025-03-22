
from scipy.optimize import minimize, linprog
import plotly.graph_objects as go
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

def simplex_generate_3d_surface(coeffs, point=None):
    a1, a2, a3, a4, a5 = coeffs
    
    x_vals = np.linspace(-3, 3, 100)
    y_vals = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x_vals, y_vals)

    Z = a1 * X**2 + a2 * Y**2 + a3 * X * Y + a4 * X + a5 * Y

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    if point is not None:
        x, y = point
        z = a1 * x**2 + a2 * y**2 + a3 * x * y + a4 * x + a5 * y

        fig.add_trace(go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode="markers",
            marker=dict(size=5, color="red"),
            name="Точка"
        ))

    fig.update_layout(
        title={
            'text': f"Функция f(x₁, x₂) = {a1}x₁² + {a2}x₂² + {a3}x₁x₂ + {a4}x₁ + {a5}x₂",
            'x': 0.5,
            'font': {'size': 18}
        },
        scene=dict(
            xaxis_title="x₁",
            yaxis_title="x₂",
            zaxis_title="f(x)"
        ),
        height=700
    )

    return fig


# x0 = [1, 1]  
# coeffs_f = [0,-1,0,1,2]  
# coeffs_con = [3,2,6,1,2,4]
# result, success, message = simplex_method(x0, coeffs_f, coeffs_con, "maximize")

# """
# x0 = [1, 1]  
# coeffs_f = [2,3,4,-6,-3]  
# coeffs_con = [1,1,1,2,3,4] 


# result, success, message = optimize(x0, coeffs_f, coeffs_con, "minimize")
# """


# print("Результат оптимизации:")
# print(f"Успешно? {'Да' if success else 'Нет'}")
# print(f"Сообщение: {message}")
# for res in result:
#     print(f"iteration = {res['iteration']}")
#     print(f"Точка: x1 = {res['x']}, x2 = {res['y']}")
#     print(f"Значение функции: f_value = {res['f_value']}")