__author__ = 'hawker'
import random
import nim_tools
import tools

class Individual(object):
    mutation_factor = 5

    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0

    @staticmethod
    def random_ind(genome_length=15):
        genome = ''.join([random.choice("01") for _ in xrange(genome_length)])
        return Individual(genome)

    def mutate_random_gene(self):
        gene_list = list(self.genome)
        which_one = random.randint(0, len(gene_list)-1)
        mutated_value = random.choice("01")
        gene_list[which_one] = mutated_value
        self.genome = "".join(gene_list)
        return which_one, mutated_value

    @staticmethod
    def decide_if_mutate():
        return Individual.mutation_factor <= random.randint(0, 100)

    def __str__(self):
        return "genome:"+self.genome+";fitness:"+str(self.fitness)+"\n"

