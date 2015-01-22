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

    def breed_with(self, another_ind):
        child1_genome, child2_genome = tools.binary_crossover_from_string(self.genome, another_ind.genome)
        child1 = Individual(child1_genome)
        child2 = Individual(child2_genome)
        return child1, child2

    def fight(self, another_ind):
        fighters = (self.genome, another_ind.genome)
        winner_index = nim_tools.nim_game_simulation(fighters)
        this_individual_won = (winner_index == 0)
        self.fitness = 1*int(this_individual_won)
        another_ind.fitness = 1*int(not this_individual_won)
        return this_individual_won

    def __str__(self):
        return "genome:"+self.genome+";fitness:"+str(self.fitness)+"\n"

