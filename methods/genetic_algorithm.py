import numpy as np

def genetic_algorithm(objective_func, bounds, used_methods={"crossover": True, "mutation": True}, population_size=50, 
             crossover_prob=0.8, mutation_prob=0.1, mutation_parameter=3,
             max_iter=100, tol=1e-6, patience=25):

    # Инициализация параметров
    history = []

    # 1. Генерация начальной популяции
    population = np.zeros((population_size, 2))
    population[:, 0] = np.random.uniform(bounds[0][0], bounds[0][1], population_size)
    population[:, 1] = np.random.uniform(bounds[1][0], bounds[1][1], population_size)
    
    best_fitness = np.inf
    no_improve = 0

    recombination_parameter = 0.25
    
    for iteration in range(max_iter):
        # 2. Вычисление пригодности
        objective_values = np.array([objective_func(ind[0], ind[1]) for ind in population])
        #print(objective_values)
        # Сохранение лучшей особи
        best_idx = np.argmin(objective_values)
        current_best = population[best_idx]
        current_value = objective_values[best_idx]
        
        # Критерий остановки
        if abs(current_value - best_fitness) < tol:
            no_improve += 1
            if no_improve >= patience:
                break
        elif current_value < best_fitness:
            no_improve = 0
            best_fitness = current_value
        
        # Запись хромосомы в историю
        history.append({
            'iteration': iteration+1,
            'x': current_best[0],
            'y': current_best[1],
            'f_value': current_value
        })
        
        fitness = 1 / (1+objective_values)
        fitness_sum = fitness.sum()
        if fitness_sum == 0:
            probabilities = np.ones(population_size) / population_size
        else:
            probabilities = fitness / fitness_sum
        
        for i in range(len(probabilities)):
            if np.isnan(probabilities[i]):
                probabilities[i] = 0
        #print(probabilities)

        # 3-6. Генерация нового поколения
        # Ваш код до изменений

        temporary_population = []
        elitism_count = int(population_size * 0.1) 

        sorted_population = sorted(zip(population, objective_values), key=lambda x: x[1])
        best_individuals = [ind for ind, _ in sorted_population[:elitism_count]]

        temporary_population.extend(best_individuals)

        while len(temporary_population) < population_size:
            # Отбор родителей (метод рулетки)            
            parents = population[np.random.choice(
                population_size, 2, p=probabilities, replace=False)]
            
            if used_methods['crossover']:
                if np.random.rand() < crossover_prob:
                    alpha1 = np.random.uniform(-recombination_parameter, 
                                                1 + recombination_parameter, 
                                                size=parents[0].shape)
                    alpha2 = np.random.uniform(-recombination_parameter, 
                                                1 + recombination_parameter, 
                                                size=parents[0].shape)
                    child1 = parents[0] + alpha1 * (parents[1] - parents[0])
                    child2 = parents[0] + alpha2 * (parents[1] - parents[0])
                else:
                    child1, child2 = parents[0], parents[1]
            else:
                child1, child2 = parents[0], parents[1]
            
            for child in [child1, child2]:
                # Мутация (мутация для вещественных особей)
                if used_methods['mutation']:
                    if np.random.rand() < mutation_prob:
                        delta = sum(2**(-i) * (np.random.rand() < (1/mutation_parameter)) for i in range(1, mutation_parameter+1))
                        
                        child[0] += delta+0.5*(bounds[0][1]-bounds[0][0]) * ((-1) if np.random.rand()<=0.5 else 1)
                        child[1] += delta+0.5*(bounds[1][1]-bounds[1][0]) * ((-1) if np.random.rand()<=0.5 else 1)
                    
                    
                    child[0] = np.clip(child[0], bounds[0][0], bounds[0][1])
                    child[1] = np.clip(child[1], bounds[1][0], bounds[1][1])
                temporary_population.append(child)

        # Обновляем популяцию
        population = np.array(temporary_population)


    # Формирование результата
    converged = True
    message = "Оптимум найден" if converged else "Достигнуто максимальное количество итераций"
    
    return history, converged, message

#genetic_algorithm(lambda x,y: x + y, [[-3,3],[-3,3]])