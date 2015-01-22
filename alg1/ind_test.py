__author__ = 'hawker'

import unittest
from individual import Individual


class MyTestCase(unittest.TestCase):

    def test_constr(self):
        ind = Individual("10101")
        self.assertEqual(ind.genome, "10101")
        self.assertEqual(ind.fitness, 0)

    def test_class(self):
        self.assertEqual(Individual.mutation_factor, 5)

    def test_random(self):
        ind1 = Individual.random_ind()
        ind2 = Individual.random_ind(20)
        self.assertEqual(len(ind1.genome), 15)
        self.assertEqual(len(ind2.genome), 20)
        self.assertEqual(ind1.fitness, 0)

    def test_mutation_decision(self):
        self.assertIn(Individual.decide_if_mutate(), [True, False])

    def test_mutation(self):
        ind1 = Individual.random_ind()
        mutated_gene_index, mutated_value = ind1.mutate_random_gene()
        self.assertEqual(ind1.genome[mutated_gene_index], mutated_value)

    def test_breeding(self):
        ind1 = Individual("111")
        ind2 = Individual("111")
        child1, child2 = ind1.breed_with(ind2)
        self.assertEqual(child1.genome, child2.genome)

    def test_fight(self):
        ind1 = Individual("01101110")
        ind2 = Individual("00111000")
        fight1 = ind2.fight(ind1)
        self.assertEqual(ind1.fitness, 1)
        self.assertEqual(ind2.fitness, 0)
        fight2 = ind1.fight(ind2)
        self.assertEqual(fight1, False)
        self.assertEqual(fight2, False)



if __name__ == '__main__':
    unittest.main()
