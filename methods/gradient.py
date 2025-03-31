import math
import numpy as np

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
