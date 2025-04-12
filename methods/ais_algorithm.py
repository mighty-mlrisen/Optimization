import numpy as np

def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def simple_ais_iteration(func, population, n_b, n_c,n_d, alpha, bounds):
    
    """
    
    Параметры:
    - func: функция.
    - population: текущая популяция.
    - n_b: число антител (особей) с наилучшей аффинностью.
    - n_c: число клонов, создаваемых для каждого лучшего антитела.
    - n_d: число клонов , оставляемых после мутации 
    - alpha: коэффициент мутации
    - bounds: ограничения.
    """
    pop_size, dim = population.shape
    
    fitness = np.array([func(ind) for ind in population])
    
    #  Из текущей популяции выбираем n_b антител с максимальной BG-аффинностью
    indices_sorted = np.argsort(fitness)
    best_indices = indices_sorted[:n_b]
    best_ants = population[best_indices] 
    best_fitnesses = fitness[best_indices] 
    
    f_min = best_fitnesses.min()
    f_max = best_fitnesses.max()
    
    clones = []
    epsilon=1e-8
    for i in range(n_b):
        alpha_i = alpha * (1 - (best_fitnesses[i] - f_min) / (f_max - f_min + epsilon))
        #alpha_i = alpha * ((best_fitnesses[i] - f_min) / (f_max - f_min + epsilon))
        original = best_ants[i]
        
        for _ in range(n_c):
            # Мутация 
            mutation = alpha_i * (np.random.rand(dim) - 0.5)
            clone = original + mutation
            clone = np.clip(clone, bounds[0], bounds[1])
            clones.append(clone)

    clones = np.array(clones)
    
    clone_fitness = np.array([func(ind) for ind in clones])

    sorted_clone_indices = np.argsort(clone_fitness)

    # Оставляем только n_d лучших клонов
    best_clones = clones[sorted_clone_indices[:n_d]]
    best_clone_fitness = clone_fitness[sorted_clone_indices[:n_d]]
    
    # Объединяем исходную популяцию и клонов
    combined = np.vstack((population, best_clones))
    combined_fitness = np.hstack((fitness, best_clone_fitness))
    
    # Сжимаем до pop_size лучших
    combined_indices_sorted = np.argsort(combined_fitness)
    best_combined_indices = combined_indices_sorted[:pop_size]
    
    new_population = combined[best_combined_indices]
    new_fitness = combined_fitness[best_combined_indices]
    
    best_idx_in_new = np.argmin(new_fitness)
    best_fitness = new_fitness[best_idx_in_new]
    best_sol = new_population[best_idx_in_new]
    
    return new_population, best_fitness, best_sol


def ais_optimize(func, dim, pop_size=30, n_b=5, n_c=10,n_d=5, alpha=0.5,
                 bounds=(-5, 5), generations=50, verbose=True):
    
    # Инициализируем популяцию
    population = np.random.uniform(bounds[0], bounds[1], (pop_size, dim))

    prev_best_fitness = None
    tol = 1e-6
    no_improve = 0
    history = []
    
    for iter in range(generations):
        # Выполняем итерацию
        population, best_fitness, best_sol = simple_ais_iteration(
            func, population, n_b, n_c,n_d, alpha, bounds
        )

        if  prev_best_fitness is None or abs(best_fitness - prev_best_fitness) < tol:
            no_improve += 1
        else:
            no_improve = 0  

        if no_improve == 25:
            break

        history.append({
            'iteration': iter + 1,
            'x': best_sol[0],
            'y': best_sol[1],
            'f_value': best_fitness
        })

        prev_best_fitness = best_fitness
    
    return history


if __name__ == "__main__":
    dim = 2  
    pop_size = 50
    n_b = 10
    n_c = 5
    n_d = 5
    alpha = 0.5
    bounds = (-5, 5)
    generations = 100
    
    history = ais_optimize(
        rosenbrock,
        dim,
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
    
    print(f"{'x, y =':<10} ({x}, {y})")
    print(f"{'f(x) =':<10} {func_value}")
    print(f"{'Итерация:':<12} {iteration}")   

    """
    for item in history:
        iteration = item['iteration']
        x = item['x']
        y = item['y']
        func_value = item['f_value']
        print(f"{iteration:<12} {x:<15} {y:<15} {func_value:<15}")
     """
