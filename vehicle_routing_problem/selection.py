import random

def select_parents(individuals_with_fitness: list) -> tuple:
    """returns pair of parents for reproduction"""
    first_parent = select_individual(individuals_with_fitness)

    individuals = [individual for (individual, _) in individuals_with_fitness]
    first_parent_index = individuals.index(first_parent)

    individuals_with_fitness.pop(first_parent_index)

    second_parent = select_individual(individuals_with_fitness)

    return (first_parent, second_parent)


def select_individual(individuals_with_fitness: list):
    fitnesses = [fitness for (_, fitness) in individuals_with_fitness]
    fitness_sum = sum(fitnesses)

    running_sum = 0

    stop_condition = random.uniform(0, fitness_sum)
    for (individual, fitness) in individuals_with_fitness:
        running_sum += fitness
        if running_sum >= stop_condition:
            return individual
    
    raise("Individual was not return")