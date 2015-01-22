__author__ = 'hawker'
import random

from individual import Individual


class Population:
    def __init__(self, size):
        self.size = size
        self.pop = []
        self.selected = []
        self.selected_indexes = []
        self.fitness_table = []
        Individual.mutation_factor = 5
        for i in xrange(size):
            self.pop.append(Individual.random_ind())

    def __str__(self):
        result = ""
        for i, ind in enumerate(self.pop):
            result += str(i)+";"+str(ind)
        return result

    def __repr__(self):
        return self.__str__()