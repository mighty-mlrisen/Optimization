import numpy as np
from methods.particleswarm.swarm import Swarm
from methods.genetic_algorithm import genetic_algorithm
from methods.particle_swarm import particle_swarm
import pandas as pd

def hybrid_optimize(
    func,
    ga_bounds,
    ps_bounds,
    ga_population_size=100,
    ga_crossover_prob=0.8,
    ga_mutation_prob=0.1,
    ga_mutation_parameter=3,
    ga_max_iter=100,
    ps_swarmsize=100,
    ps_max_iter=100,
    ps_current_velocity=0.5,
    ps_local_ratio=2,
    ps_global_ratio=5,
    ps_penalty=10000
):
    # Запуск GA
    ga_history, ga_converged, ga_message, ga_population = genetic_algorithm(
        objective_func=func, 
        bounds=ga_bounds, 
        population_size=ga_population_size,
        crossover_prob=ga_crossover_prob,
        mutation_prob=ga_mutation_prob,
        mutation_parameter=ga_mutation_parameter,
        max_iter=ga_max_iter+10
    )
    
    """
    scored_population = [(individual, func(*individual)) for individual in ga_population]

    sorted_population = sorted(scored_population, key=lambda x: x[1])

    best_individuals = [individual for individual, _ in sorted_population[:ps_swarmsize]]
    """
    
    wrapped_func = lambda pos: func(*pos)
    
    # Запуск PS
    ps_history, ps_converged, ps_message = particle_swarm(
        func=wrapped_func,
        iter_count=ps_max_iter+5,
        swarm_size=ps_swarmsize,
        bounds=ps_bounds,
        current_velocity_ratio=ps_current_velocity,
        local_velocity_ratio=ps_local_ratio,
        global_velocity_ratio=ps_global_ratio,
        penalty_ratio=ps_penalty,
        init_population=ga_population
        
    )
    # Объединение истории
    combined_history = ga_history.copy()
    last_iter = ga_history[-1]['iteration'] if ga_history else 0

    """
    combined_history.append({
            'iteration': "переход",
            'x': "переход",
            'y': "переход",
            'f_value': "переход"
        })
    """
    
    for ps_point in ps_history:
        combined_history.append({
            'iteration': last_iter + ps_point['iteration'],
            'x': ps_point['x'],
            'y': ps_point['y'],
            'f_value': ps_point['f_value']
        })
    
    return combined_history, ps_converged, f"GA: {ga_message}, PS: {ps_message}", last_iter




"""
#f = lambda x, y: (1-x)**2 + 100*((y-x**2)**2)
#f = lambda x, y: (x**2 + y - 11)**2 + (x + y**2 - 7)**2
f = lambda x, y: 20 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))
#f = lambda x, y: (x**2 + y**2)

#ga_bounds = np.array([[-3, 3], [-3, 3]])
#ps_bounds = np.array([[-3, -3], [3, 3]])

ga_bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])
ps_bounds = np.array([[-5.12, -5.12], [5.12, 5.12]])

history, converged, message = hybrid_optimize(
    func=f,
    ga_bounds=ga_bounds,
    ps_bounds=ps_bounds
)

print("Оптимизация завершена.")
print("Сошлось:", converged)
print("Сообщение:", message)
print("Последняя запись в истории:")
print(history[-1])


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.DataFrame(history)
print(df)
"""