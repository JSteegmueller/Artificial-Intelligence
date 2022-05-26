# Assignment 5, Question 3, AI 2021/22
# Genetic Algorithm on n-Queens-problem
# Group members:
# 1) 
# 2) 


import random
import math
import numpy as np
import copy

# keep this for some test cases
np.random.seed(2021)
i1 = [1, 1, 1, 1, 1, 1, 1, 1]
i2 = [1, 2, 3, 4, 5, 6, 7, 8]
i3 = [2, 4, 7, 4, 8, 5, 5, 2]


# a) ****************
def initialize_population(population_size, num_queens):
    """
    Args:
        population_size: number of samples to generate
        num_queens:  (board size)

    Returns:
        a list of generated population with each element having
        `num_queens` items
    """
    population = []
    for i in range(population_size):
        unit = []
        for j in range(num_queens):
            unit.append(np.random.randint(1, num_queens + 1))
        population.append(copy.copy(unit))
    return population

# testing initialize_population
print("initialize_population:")
pop1 = initialize_population(10, 8)
print(pop1)


# b) ****************
def find_conflicts(individual):
    """
    Args:
        individual (board state): a list of size `num_queens` containing each queen position

    Returns:
        Total number of conflicts with the current placement of queens
    """
    c = 0
    ss = copy.copy(individual)
    for n in individual:
        ss.pop(0)
        np = nm = n
        for nn in ss:
            nm -= 1
            np += 1
            if n == nn or nm == nn or np == nn:
                c += 1
    return c


# testing find_conflicts
print("find_conflicts:")
print(find_conflicts(i1))
print(find_conflicts(i2))
print(find_conflicts(i3))


# c) ****************
# To Solve this part, complete following three functions
#  - `fitness_function`
#  - `selection_probability`
#  - `randomSelect`
def fitness_function(individual, lamda):
    """
    Args:
        individual: current state of the board (a list)
        lamda: lambda value.

    Returns:
        fitness of current state of board, i.e. fitness of current individual
    """
    return math.exp(-lamda * find_conflicts(individual))


# Testing of fitness function
print("fitness function:")
print(fitness_function(i1, 0.1))
print(fitness_function(i2, 0.1))
print(fitness_function(i3, 0.1))


def selection_probability(fitness_population):
    """
    Args:
        fitness_population: a list of fitness values for each individual of population

    Returns:
        probability of each individual being chosen, i.e. p_i = f_i / \sum_{j} f_j
    """
    sum_fitness = sum(fitness_population)
    probabilities = []
    for x in fitness_population:
        probabilities.append(x/sum_fitness)
    return probabilities


# testing roulette-wheel
print("selection_probability:")
print(selection_probability([0.4, 0.2, 0.5]))


def random_select(population, lamda):
    """
     Randomly chooses the parent from the population using the fitness function
     steps:
     i- compute fitness of each individual using fitness_function
     ii- compute selection probability using selection_probability function
     iii- select invididual according to probability using np.random.choice function

    Args:
        population: given the list of population generated using initialize population
        lamda: for the exponential distribution

    Returns:
        selected individual
    """
    fitness = []
    for x in population:
        fitness.append(fitness_function(x, lamda))
    probs = selection_probability(fitness)

    idx = np.random.choice(range(len(population)), p=probs)
    return population[idx]


# testing random_select
print("random_select:")
print(random_select(pop1, 0.2))


# d) ****************
def cross_over(parents):
    """
    generate an offspring by combining parts of each parent
    hint: generate a random index for each parent and use it to select slices from each parent
    Args:
        parents: list of individuals

    Returns:
        a new individual
    """
    offspring = []
    crossover_points = [0]
    for _ in range(len(parents) -1 ):
        crossover_points.append(np.random.randint(0, len(parents[0])))
    crossover_points.sort()
    crossover_points.append(len(parents[0]))
    offspring = []
    for p in parents:
        offspring.extend(p[crossover_points[0]:crossover_points[1]])
        crossover_points.pop(0)
    return offspring      


# testing cross_over
print("cross_over:")
print(cross_over([i1, i2, i3]))


# e) ****************
def mutate(individual):
    """
    mutate a given individual, i.e. for each queen change its position with probability 1/n
    i.e. generate a random number using random.random and if it is less than 1/n assign
    the queen a random position other-wise leave it. 
    Args:
        individual: list of queen positions

    Returns:
        a mutated child
    """
    for idx, _ in enumerate(individual):
        if random.random() < 1/individual[idx]:
            individual[idx] = np.random.randint(1, len(individual) + 1)
    return individual


# testing mutate
print("mutate:")
print(mutate(i1))
print(mutate(i2))
print(mutate(i3))


# f) ****************
def genetic_algorithm(population_size, lamda, num_parents, queens):
    """
    Generate the solution using genetic algorithm for input population and lambda
    Your solution should generate at most 1000 generations, if no solution found
    it should return False
    Args:
        population_size: sets the number of individuals in a population
        lamda: decaying factor
        num_parents: sets the number of parents needed to reproduce

    Returns:
        - an individual with zero conflicts
        - the amount of individuals (population size * number of generations) it took to find it.
    """
    population = initialize_population(population_size, queens)
    generations = 0
    while True:
        if generations > 999:
            return False, generations * population_size
        new_population = []
        for _ in population:
            parents = []
            for _ in range(num_parents):
                parents.append(random_select(population, lamda))
            child = cross_over(parents)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        population.sort(key=lambda x:find_conflicts(x))
        generations += 1
        if find_conflicts(population[0]) == 0:
            return population[0], generations * population_size

# testing genetic algorithm

print(genetic_algorithm(10, 0.9, 2, 4))
print(genetic_algorithm(20, 0.9, 2, 4))
print(genetic_algorithm(10, 0.45, 2, 4))
print(genetic_algorithm(10, 0.9, 4, 4))

print(genetic_algorithm(10, 0.9, 2, 8))
print(genetic_algorithm(20, 0.9, 2, 8))
print(genetic_algorithm(10, 0.45, 2, 8))
print(genetic_algorithm(10, 0.9, 4, 8))

print(genetic_algorithm(10, 0.9, 2, 12))
print(genetic_algorithm(20, 0.9, 2, 12))
print(genetic_algorithm(10, 0.45, 2, 12))
print(genetic_algorithm(10, 0.9, 4, 12))


