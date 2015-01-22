__author__ = 'hawker'
import random


def binary_crossover_from_string(val1, val2, crossover_point=None):
    if crossover_point is None:
        crossover_point = random.randint(0, len(val1))
    bin1, bin2 = val1[:crossover_point]+val2[crossover_point:], val2[:crossover_point]+val1[crossover_point:]
    return bin1, bin2

