import math
import numpy as np
import plotly.graph_objects as go

#функция f(x) = 2*x_1^2 + x1*x2 + x_2^2
def f(point):
    x1 = point[0]
    x2 = point[1]
    return 2 * x1**2 + x1 * x2 + x2**2


def gradient(point, h = 1e-6):
    x1 = point[0]
    x2 = point[1]
    grad_x1 = (f([x1 + h, x2]) - f([x1 - h, x2])) / (2 * h)
    grad_x2 = (f([x1, x2 + h]) - f([x1, x2 - h])) / (2 * h)
    return [grad_x1, grad_x2]

def vector_norm(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)


def gradient_descent_method(initial_point,step, epsilon, epsilon1, epsilon2, M):
    k = 0  
    current_point = initial_point.copy()   
    point_history = []
    norm_history = []
    
    while True:
        grad = gradient(current_point)
        point_history.append(current_point.copy())
        
        grad_norm = vector_norm(grad)
        norm_history.append(grad_norm)
        if grad_norm < epsilon1:
            return {"min_point": current_point, "min_value": f(current_point), "iterations": k, "point_history": point_history,"norm_history": norm_history,"condition": "grad_norm < epsilon1"}
        
        if k >= M:
            return {"min_point": current_point, "min_value": f(current_point), "iterations": k, "point_history": point_history,"norm_history": norm_history,"condition": "k >= M"}
        
        tk = step
        while True:
            next_point = [current_point[0] - tk * grad[0], current_point[1] - tk * grad[1]]
            if ((f(next_point) - f(current_point) < 0) or (abs(f(next_point) - f(current_point)) < epsilon * grad_norm**2)):
                break
            else:
                tk /= 2

        if vector_norm([next_point[0] - current_point[0], next_point[1] - current_point[1]]) < epsilon2 and \
           abs(f(next_point) - f(current_point)) < epsilon2:
            point_history.append(next_point.copy())
            grad = gradient(next_point)
            norm_history.append(vector_norm(grad))
            return {"min_point": next_point, "min_value": f(next_point), "iterations": k, "point_history": point_history,"norm_history": norm_history,"condition": "разность значений функций < eps2"}
            
        current_point = next_point
        k += 1

def gradient_generate_3d_surface(path=None):
    x_vals = np.linspace(-3, 3, 100)
    y_vals = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    Z = 2 * X**2 + X * Y + Y**2
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    
    if path:
        x_path = [point[0] for point in path]
        y_path = [point[1] for point in path]
        z_path = [2 * x**2 + x * y + y**2 for x, y in path]
        
        fig.add_trace(go.Scatter3d(
            x=x_path,
            y=y_path,
            z=z_path,
            mode="markers+lines",
            marker=dict(size=5, color="red"),
            name="Gradient Descent Path"
        ))

    fig.update_layout(
        title={
            'text': "функция f(x₁, x₂) = 2x₁² + x₁x₂ + x₂²",
            'x': 0.5,
            'font': {'size': 18}
        },
        scene=dict(
            xaxis_title="x₁",
            yaxis_title="x₂",
            zaxis_title="f(x)"
        )
    )
    
    return fig

