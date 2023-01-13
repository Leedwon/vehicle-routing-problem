import random

def select_parents(individuals_with_fitness: list) -> tuple:
    """returns pair of parents for reproduction"""
    first_parent = select_one(individuals_with_fitness)

    individuals_with_fitness.remove(first_parent)

    second_parent = select_one(individuals_with_fitness)

    return (first_parent[0], second_parent[0])


def select_one(individuals_with_fitness: list):
    fitnesses = [fitness for (individual, fitness) in individuals_with_fitness]
    fitness_sum = sum(fitnesses)

    running_sum = 0

    stop_condition = random.uniform(0, fitness_sum)
    for (individual, fitness) in individuals_with_fitness:
        running_sum += fitness
        if running_sum >= stop_condition:
            return (individual, fitness) # returning both individual and fitness so it can be removed from the original list. It's a bit cheesy, but good enough for now.
    
    raise("Individual was not return")