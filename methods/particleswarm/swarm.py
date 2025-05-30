from abc import ABCMeta, abstractmethod

import numpy
import numpy.random

from methods.particleswarm.particle import Particle
#from particleswarm.particle import Particle



class Swarm (object):
    __metaclass__ = ABCMeta

    def __init__ (self, 
            func,
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio,
            penaltyRatio):
        """
        swarmsize - размер роя (количество частиц)
        minvalues - список, задающий минимальные значения для каждой координаты частицы
        maxvalues - список, задающий максимальные значения для каждой координаты частицы
        currentVelocityRatio - общий масштабирующий коэффициент для скорости
        localVelocityRatio - коэффициент, задающий влияние лучшей точки, найденной частицей на будущую скорость
        globalVelocityRatio - коэффициент, задающий влияние лучшей точки, найденной всеми частицами на будущую скорость
        """
        self.__func = func
        self.__swarmsize = swarmsize

        assert len (minvalues) == len (maxvalues)
        assert (localVelocityRatio + globalVelocityRatio) > 4

        self.__minvalues = numpy.array (minvalues[:])
        self.__maxvalues = numpy.array (maxvalues[:])

        self.__currentVelocityRatio = currentVelocityRatio
        self.__localVelocityRatio = localVelocityRatio
        self.__globalVelocityRatio = globalVelocityRatio

        self.__globalBestFinalFunc = None
        self.__globalBestPosition = None
        
        self._penaltyRatio = penaltyRatio

        self.__swarm = self.__createSwarm ()


    def __getitem__ (self, index):
        """
        Возвращает частицу с заданным номером
        """
        return self.__swarm[index]


    def __createSwarm (self):
        """
        Создать рой из частиц со случайными координатами
        """
        return [Particle (self) for _ in range (self.__swarmsize) ]



    def nextIteration (self):
        """
        Выполнить следующую итерацию алгоритма
        """
        for particle in self.__swarm:
            particle.nextIteration (self)


    @property
    def minvalues (self):
        return self.__minvalues


    @property
    def maxvalues (self):
        return self.__maxvalues


    @property
    def currentVelocityRatio (self):
        return self.__currentVelocityRatio


    @property
    def localVelocityRatio (self):
        return self.__localVelocityRatio


    @property
    def globalVelocityRatio (self):
        return self.__globalVelocityRatio


    @property
    def globalBestPosition (self):
        return self.__globalBestPosition


    @property
    def globalBestFinalFunc (self):
        return self.__globalBestFinalFunc
    
    @property
    def getSwarm (self):
        return self.__swarm


    def getFinalFunc (self, position):
        assert len (position) == len (self.minvalues)

        finalFunc = self._finalFunc (position)

        if (self.__globalBestFinalFunc is None or
                finalFunc < self.__globalBestFinalFunc):
            self.__globalBestFinalFunc = finalFunc
            self.__globalBestPosition = position[:]
        return finalFunc


    def _finalFunc (self, position):
        return self.__func(position) + self._getPenalty(position)

    
    @property
    def dimension (self):
        """
        Возвращает текущую размерность задачи
        """
        return len (self.minvalues)


    def _getPenalty (self, position):
        """
        Рассчитать штрафную функцию
        position - координаты, для которых рассчитывается штраф
        ratio - вес штрафа
        """
        penalty1 = sum ([self._penaltyRatio * abs (coord - minval)
            for coord, minval in zip (position, self.minvalues) 
            if coord < minval ] )

        penalty2 = sum ([self._penaltyRatio * abs (coord - maxval)
            for coord, maxval in zip (position, self.maxvalues) 
            if coord > maxval ] )

        return penalty1 + penalty2
