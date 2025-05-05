import numpy as np

def initialize_population(population_size, x_min, x_max):
    return np.random.uniform(x_min, x_max, (population_size, 2))

def chemotaxis(bacteria, func, step_size, population_size, x_min, x_max, health, chemotaxis_count, t_chemotaxis):
    """Хемотаксис с плаванием и кувырканием"""
    if chemotaxis_count >= t_chemotaxis:
        return bacteria
    
    new_bacteria = np.copy(bacteria)
    fitness = np.array([func(b) for b in bacteria])
    
    for i in range(population_size):
        # Кувыркание
        direction = np.random.uniform(-1, 1, 2)
        direction = direction / np.linalg.norm(direction)
        
        candidate = bacteria[i] + step_size * direction
        candidate = np.clip(candidate, x_min, x_max)
        
        if func(candidate) > fitness[i]:
            new_bacteria[i] = candidate
            health[i] += func(candidate)
    
    return new_bacteria

def reproduction(bacteria, population_size, health, reproduction_count, t_reproduction):
    """Репродукция"""

    if reproduction_count >= t_reproduction:
        return bacteria
    
    sorted_indices = np.argsort(health)[::-1]
    best_bacteria = bacteria[sorted_indices[:population_size//2]]
    new_population = np.repeat(best_bacteria, 2, axis=0)
    
    return new_population

def elimination_dispersal(bacteria, elimination_num, elimination_prob, population_size, x_min, x_max, elimination_count, t_elimination):
    """Ликвидация и рассеивание"""

    if elimination_count >= t_elimination:
        return bacteria
    
    new_bacteria = np.copy(bacteria)
    
    for _ in range(elimination_num):
        if np.random.rand() < elimination_prob:
            i = np.random.randint(0, population_size)
            new_bacteria[i] = np.random.uniform(x_min, x_max, 2)
    
    return new_bacteria

def bacterial_foraging_optimization(
        func,                  # Фитнес-функция
        population_size = 50,  # Четное число бактерий
        bounds = [-5, 5],    # x_min и x_max - границы для каждой координаты
        t_chemotaxis = 100,  # Число шагов хемотаксиса
        t_reproduction = 5,   # Число шагов репродукции
        t_elimination = 2,    # Число шагов ликвидации/рассеивания
        step_size = 0.1,      # Начальный размер шага хемотаксиса
        elimination_prob = 0.1,  # Вероятность ликвидации бактерии
        elimination_num = 5,     # Число уничтожаемых бактерий
    ):

    x_min, x_max = bounds[0], bounds[1]
    
    bacteria = initialize_population(population_size, x_min, x_max)
    best_solution = None
    best_fitness = -np.inf

    history = []
    chemotaxis_count = 0
    reproduction_count = 0
    elimination_count = 0

    # prev_best_fitness = best_fitness

    for i in range(t_chemotaxis):
        health = np.array([func(b) for b in bacteria]) 
        bacteria = chemotaxis(bacteria, func, step_size * (1 - i/t_chemotaxis), population_size, x_min, x_max, health, chemotaxis_count, t_chemotaxis)
        bacteria = reproduction(bacteria, population_size, health, reproduction_count, t_reproduction)
        bacteria = elimination_dispersal(bacteria, elimination_num, elimination_prob, population_size, x_min, x_max, elimination_count, t_elimination)

        current_fitness = np.array([func(b) for b in bacteria])
        best_idx = np.argmax(current_fitness)
        
        if current_fitness[best_idx] > best_fitness:
                 best_fitness = current_fitness[best_idx]
                 best_solution = bacteria[best_idx]
                 
        history.append({
                    "iteration": i + 1,
                    "x": best_solution[0],
                    "y": best_solution[1],
                    "f_value": best_fitness
                })

        # if (abs(best_fitness - prev_best_fitness) < 1e-6 and best_fitness != prev_best_fitness):
        #     break
        
        # prev_best_fitness = best_fitness
        
        chemotaxis_count += 1
        reproduction_count += 1
        elimination_count += 1      
    
    message = "Оптимум найден"
    converged = True

    return history, converged, message