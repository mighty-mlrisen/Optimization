from methods.particleswarm.swarm import Swarm
#from particleswarm.swarm import Swarm
import numpy as np

def particle_swarm(func, iter_count, swarm_size, bounds, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio, penalty_ratio,tol=1e-6,init_population=None):
    history = []

    swarm = Swarm (
            func,
            swarm_size, 
            bounds[0][:], 
            bounds[1][:],
            current_velocity_ratio,
            local_velocity_ratio, 
            global_velocity_ratio,
            penalty_ratio,
        )
    best_swarm_fitness = np.inf
    patience = 25
    no_improve = 0

    if init_population is not None:
        for i, pos in enumerate(init_population):
            if i < len(swarm.getSwarm):
                swarm.getSwarm[i].position = np.array(pos)
                swarm.getSwarm[i].localBestPosition = np.array(pos)
                swarm.getSwarm[i].localBestFinalFunc = swarm.getFinalFunc(pos)
    
    for i in range(iter_count):
        swarm.nextIteration()

        current_value = swarm.globalBestFinalFunc

        if abs(current_value - best_swarm_fitness) < tol:
            no_improve += 1
            #if no_improve >= patience:
                #break
        elif current_value < best_swarm_fitness:
            no_improve = 0  
            best_swarm_fitness = current_value

        history.append({
            'iteration': i+1,
            'x': swarm.globalBestPosition[0],
            'y': swarm.globalBestPosition[1],
            'f_value': swarm.globalBestFinalFunc
        })

    converged = True
    message = "Оптимум найден" if converged else "Достигнуто максимальное количество итераций"
    
    return history, converged, message

def rosenbrock(position):
    x, y = position
    return (1-x)**2 + 100*((y-x**2)**2)

# как передавать лямбду (не знаю как нормально реализовать)
#history, converged, message = particle_swarm(lambda pos: (1-pos[0])**2 + 100*((pos[1]-pos[0]**2)**2), 100, 100, [[-3, -3], [3, 3]], 0.5, 2, 5, 10000) 

# можно передавать обычную функцию от списка position
#history, converged, message = particle_swarm(func=rosenbrock, iter_count=100, swarm_size=100, bounds=[[-3, -3], [3, 3]], current_velocity_ratio=0.5, local_velocity_ratio=2, global_velocity_ratio=5, penalty_ratio=10000) 

#print(history)