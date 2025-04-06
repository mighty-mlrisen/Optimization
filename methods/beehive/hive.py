from typing import List, Optional
from methods.beehive.bee import FloatBee

class Hive:
    """Улей. Управляет пчелами"""
    def __init__(
        self,
        func,
        scout_bee_count: int,
        selected_bee_count: int,
        best_bee_count: int,
        sel_sites_count: int,
        best_sites_count: int,
        range_list: List[float],
        minval: List[float],
        maxval: List[float]
    ):
        """
        :param scout_bee_count: Количество пчел-разведчиков
        :param selected_bee_count: количество пчел, посылаемое на один из лучших участков
        :param best_bee_count: количество пчел, посылаемое на остальные выбранные участки
        :param sel_sites_count: количество выбранных участков
        :param best_sites_count: количество лучших участков среди выбранных
        :param bee_type: класс пчелы, производный от FloatBee
        :param range_list: список диапазонов координат для одного участка
        """
        self.scout_bee_count = scout_bee_count
        self.selected_bee_count = selected_bee_count
        self.best_bee_count = best_bee_count        
        
        self.sel_sites_count = sel_sites_count
        self.best_sites_count = best_sites_count
        
        self.bee_type = FloatBee
        self.range = range_list
        
        # Лучшая на данный момент позиция
        self.best_position: Optional[List[float]] = None
        
        # Лучшее на данный момент здоровье пчелы (чем больше, тем лучше)
        self.best_fitness: float = -1.0e9
        
        # Начальное заполнение роя пчелами со случайными координатами
        bee_count = scout_bee_count + selected_bee_count * sel_sites_count + best_bee_count * best_sites_count
        self.swarm: List[FloatBee] = [FloatBee(func, minval, maxval) for _ in range(bee_count)]
        
        # Лучшие и выбранные места
        self.best_sites: List[FloatBee] = []
        self.sel_sites: List[FloatBee] = []
        
        self.swarm.sort(reverse=True)        
        self.best_position = self.swarm[0].get_position()
        self.best_fitness = self.swarm[0].fitness
    
    def send_bees(self, position: List[float], index: int, count: int) -> int:
        """Послать пчел на позицию.
        :return: номер следующей пчелы для вылета
        """
        for _ in range(count):
            if index == len(self.swarm):
                break
            
            curr_bee = self.swarm[index]
            
            if curr_bee not in self.best_sites and curr_bee not in self.sel_sites:
                curr_bee.goto(position, self.range)
            
            index += 1
        
        return index
    
    def next_step(self) -> None:
        """Новая итерация"""        
        # Выбираем самые лучшие места и сохраняем ссылки на тех, кто их нашел
        self.best_sites = [self.swarm[0]]
        
        curr_index = 1
        for curr_bee in self.swarm[curr_index:]:
            if curr_bee.other_patch(self.best_sites, self.range):
                self.best_sites.append(curr_bee)
                        
                if len(self.best_sites) == self.best_sites_count:
                    break
                
            curr_index += 1
        
        self.sel_sites = []
        
        for curr_bee in self.swarm[curr_index:]:
            if (curr_bee.other_patch(self.best_sites, self.range) and 
                curr_bee.other_patch(self.sel_sites, self.range)):
                self.sel_sites.append(curr_bee)
                    
                if len(self.sel_sites) == self.sel_sites_count:
                    break
                    
        # Отправляем пчел на задание
        bee_index = 1  # 0-ую пчелу никуда не отправляем
        
        for best_bee in self.best_sites:
            bee_index = self.send_bees(best_bee.get_position(), bee_index, self.best_bee_count)
            
        for sel_bee in self.sel_sites:
            bee_index = self.send_bees(sel_bee.get_position(), bee_index, self.selected_bee_count)    

        # Оставшихся пчел пошлем куда попадет
        for curr_bee in self.swarm[bee_index:]:
            curr_bee.goto_random()
    
        self.swarm.sort(reverse=True)        
        self.best_position = self.swarm[0].get_position()
        self.best_fitness = self.swarm[0].fitness