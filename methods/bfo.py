import numpy as np

# def objective_function(x):
#     return -np.sum(x**2)

def initialize_population(population_size, x_min, x_max):
    return np.random.uniform(x_min, x_max, (population_size, 2))

def chemotaxis(bacteria, func, step_size, population_size, x_min, x_max):
    """Локальный поиск с плаванием и кувырканием"""
    new_bacteria = np.copy(bacteria)
    fitness = np.array([func(b) for b in bacteria])
    
    for i in range(population_size):
        # Выбираем направление движения (плавание или кувырок)
        if np.random.rand() > 0.5:  # Плавание
            direction = np.random.uniform(-1, 1, 2)
            direction = direction / np.linalg.norm(direction)  # Нормализация
        else:  # Кувырок
            direction = np.random.uniform(-1, 1, 2)
        
        # Делаем шаг
        candidate = bacteria[i] + step_size * direction
        
        # Проверяем границы
        candidate = np.clip(candidate, x_min, x_max)
        
        # Принимаем шаг, если улучшили значение функции
        if func(candidate) > fitness[i]:
            new_bacteria[i] = candidate
    
    return new_bacteria

def reproduction(bacteria, func, population_size):
    """Размножение наиболее успешных бактерий"""
    # Вычисляем "здоровье" каждой бактерии (сумму значений функции)
    health = np.array([func(b) for b in bacteria])
    
    # Сортируем бактерии по здоровью
    sorted_indices = np.argsort(health)[::-1]  # Убывающий порядок
    
    # Первая половина - лучшие бактерии, вторая - худшие
    best_bacteria = bacteria[sorted_indices[:population_size//2]]
    
    # Каждая лучшая бактерия делится на две
    new_population = np.repeat(best_bacteria, 2, axis=0)
    
    return new_population

def elimination_dispersal(bacteria, elimination_num, elimination_prob, population_size, x_min, x_max):
    """Уничтожение и случайное перемещение части бактерий"""
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
    """Основная функция алгоритма BFO"""
    # Инициализация популяции
    x_min, x_max = bounds[0], bounds[1]
    
    bacteria = initialize_population(population_size, x_min, x_max)
    best_solution = None
    best_fitness = -np.inf

    history = []

    # Основной цикл алгоритма
    for l in range(t_elimination):
        for r in range(t_reproduction):
            for t in range(t_chemotaxis):
                # Хемотаксис
                bacteria = chemotaxis(bacteria, func, step_size * (1 - t/t_chemotaxis), population_size, x_min, x_max)
                
                # Обновляем лучшее решение
                current_fitness = np.array([func(b) for b in bacteria])
                best_idx = np.argmax(current_fitness)
                if current_fitness[best_idx] > best_fitness:
                    best_fitness = current_fitness[best_idx]
                    best_solution = bacteria[best_idx]
                history.append({
                    "x": best_solution[0],
                    "y": best_solution[1],
                    "f_value": best_fitness
                })
            
            # Репродукция
            bacteria = reproduction(bacteria, func, population_size)
        
        # Ликвидация и рассеивание
        bacteria = elimination_dispersal(bacteria, elimination_num, elimination_prob, population_size, x_min, x_max)
    
    message = f"Оптимум f(x,y)={best_fitness} найден в точке ({best_solution[0]}, {best_solution[1]})."

    return history, message

history, message = bacterial_foraging_optimization(
        func = lambda point: -np.sum(point**2),
        population_size = 50,  # Четное число бактерий
        bounds = [-5, 5],     # x_min и x_max - границы для каждой координаты
        t_chemotaxis = 100,  # Число шагов хемотаксиса
        t_reproduction = 5,   # Число шагов репродукции
        t_elimination = 2,    # Число шагов ликвидации/рассеивания
        step_size = 0.1,      # Начальный размер шага хемотаксиса
        elimination_prob = 0.1,  # Вероятность ликвидации бактерии
        elimination_num = 5,     # Число уничтожаемых бактерий
    )


print(message)