from typing import List
import random

class FloatBee:
    """Класс пчел, где в качестве координат используется список вещественных чисел"""
    def __init__(self, func, minval, maxval):
        self.func = func
        
        self.minval: List[float] = minval
        self.maxval: List[float] = maxval

        self.position = [random.uniform (self.minval[n], self.maxval[n]) for n in range (2) ]
        self.calcfitness()
        
    def calcfitness(self) -> None:
        self.fitness = self.func(self.position)
        
    def __lt__(self, other: 'FloatBee') -> bool:
        """Функция для сортировки пчел по их целевой функции (здоровью) в порядке убывания."""
        return self.fitness < other.fitness
            
    def other_patch(self, bee_list: List['FloatBee'], range_list: List[float]) -> bool:
        """Проверить находится ли пчела на том же участке, что и одна из пчел в bee_list. 
        range_list - интервал изменения каждой из координат"""
        if not bee_list:
            return True
        
        for curr_bee in bee_list:
            position = curr_bee.get_position()
            
            for n in range(len(self.position)):
                if abs(self.position[n] - position[n]) > range_list[n]:
                    return True
        
        return False
    
    def get_position(self) -> List[float]:
        """Вернуть копию (!) своих координат"""
        return [val for val in self.position]
        
    def goto(self, other_pos: List[float], range_list: List[float]) -> None:
        """Перелет в окрестность места, которое нашла другая пчела. Не в то же самое место!"""

        # К каждой из координат добавляем случайное значение
        self.position = [
            other_pos[n] + random.uniform(-range_list[n], range_list[n])
            for n in range(len(other_pos))
        ]
        
        # Проверим, чтобы не выйти за заданные пределы
        self.check_position()
        
        # Рассчитаем и сохраним целевую функцию
        self.calcfitness()
        
    def goto_random(self) -> None:
        """Заполнить координаты случайными значениями"""
        self.position = [
            random.uniform(self.minval[n], self.maxval[n]) 
            for n in range(len(self.position))
        ]
        self.check_position()
        self.calcfitness()    
        
    def check_position(self) -> None:
        """Скорректировать координаты пчелы, если они выходят за установленные пределы"""
        for n in range(len(self.position)):
            if self.position[n] < self.minval[n]:
                self.position[n] = self.minval[n]
            elif self.position[n] > self.maxval[n]:
                self.position[n] = self.maxval[n]