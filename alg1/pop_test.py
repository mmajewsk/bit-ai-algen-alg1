__author__ = 'hawker'

import unittest
from population import Population


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        pop1 = Population(4)
        self.assertEqual(len(pop1.pop), 4)
        self.assertEqual(pop1.size, 4)
        self.assertEqual(pop1.selected, [])
        self.assertEqual(pop1.selected_indexes, [])
        self.assertEqual(pop1.fitness_table, [])
        self.assertEqual(pop1.pop[0].mutation_factor, 5)

    def test_evalutaion(self):
        pop1 = Population(4)
        result = pop1.evaluate()
        self.assertEqual(len(pop1.fitness_table), 4)
        self.assertEqual(pop1.fitness_table, result)
        self.assertIn(pop1.pop[0].fitness, [0, 1])
        self.assertEqual(pop1.pop[0].fitness, result[0])

    def test_selection(self):
        pop1 = Population(4)
        result = pop1.evaluate()
        indexes, selected = pop1.selection()
        self.assertEqual(pop1.selected_indexes, indexes)
        self.assertEqual(pop1.selected, selected)
        self.assertEqual(len(selected), 2)
        self.assertEqual(len(indexes), 2)
        for ind in selected:
            self.assertEqual(ind.fitness, 1)
        for i in indexes:
            self.assertEqual(pop1.pop[i].fitness,1)

    def test_breeding(self):
        pop1 = Population(4)
        result = pop1.evaluate()
        pop1.selection()
        pop1.breed()
        self.assertEqual(len(pop1.pop), 4)
        self.assertEqual(pop1.selected, [])
        self.assertEqual(pop1.selected_indexes, [])
        self.assertEqual(pop1.fitness_table, [])

    def test_evolve(self):
        pop1 = Population(4)
        pop1.evolve()
        self.assertEqual(len(pop1.pop), 4)
        self.assertEqual(pop1.selected, [])
        self.assertEqual(pop1.selected_indexes, [])
        self.assertEqual(pop1.fitness_table, [])




if __name__ == '__main__':
    unittest.main()
