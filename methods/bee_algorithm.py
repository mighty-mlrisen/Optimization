from typing import List
from methods.beehive.hive import Hive
import numpy as np

def bee_algorithm(
        func,
        scout_bee_count: int,
        selected_bee_count: int,
        best_bee_count: int,
        sel_sites_count: int,
        best_sites_count: int,
        range_list: List[float],
        minval: List[float],
        maxval: List[float],
        max_iter: int
):
    hive = Hive(
        func, 
        scout_bee_count, 
        selected_bee_count,
        best_bee_count, 
        sel_sites_count, 
        best_sites_count, 
        range_list,
        minval,
        maxval
    )
    
    history = []
    no_improve = 0
    prev_best_fitness = None
    
    tol = 1e-6
    
    for iter in range(max_iter):
        hive.next_step()
        
        if prev_best_fitness is None or abs(hive.best_fitness - prev_best_fitness) < tol:
            no_improve += 1
        else:
            no_improve = 0    
        
        # if no_improve == 25:
        #     break
        
        history.append({
            'iteration': iter + 1,
            'x': hive.swarm[0].position[0],
            'y': hive.swarm[0].position[1],
            'f_value': hive.best_fitness
        })
        
        prev_best_fitness = hive.best_fitness
        
        
    converged = True
    message = "Оптимум найден" if converged else "Достигнуто максимальное количество итераций"

    return history, converged, message


'''
def rosenbrock(position):
    x, y = position
    return -((1-x)**2 + 100*((y-x**2)**2))

def rastrygin(position):
    x, y = position
    return -(20 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)))


scoutbeecount = 300
selectedbeecount = 10
bestbeecount = 30
selsitescount = 15
bestsitescount = 5
max_iter = 1000

range_list = [100, 100]

minval = [-20, -20]
maxval = [20, 20]

history = bee_algorithm(rosenbrock, scoutbeecount, selectedbeecount, bestbeecount, selsitescount, bestsitescount, range_list, minval, maxval, max_iter)
print(history)
'''