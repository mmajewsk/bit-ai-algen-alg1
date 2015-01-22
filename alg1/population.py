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

    def evaluate(self):
        self.fitness_table = []
        random.shuffle(self.pop)
        for i in xrange(0, self.size, 2):
            self.pop[i].fight(self.pop[i+1])
            self.fitness_table.append(self.pop[i].fitness)
            self.fitness_table.append(self.pop[i+1].fitness)
        return self.fitness_table

    def selection(self):
        survived_table = []
        for i, ind in enumerate(self.pop):
            if ind.fitness:
                survived_table.append(ind)
                self.selected_indexes.append(i)
        self.selected = survived_table
        return self.selected_indexes, self.selected

    def __str__(self):
        result = ""
        for i, ind in enumerate(self.pop):
            result += str(i)+";"+str(ind)
        return result

    def __repr__(self):
        return self.__str__()