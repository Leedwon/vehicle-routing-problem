from vehicle_routing_problem.fitness import fitness


from vehicle_routing_problem.initial_population_factory import create_initial_population
from vehicle_routing_problem.mutation import mutate
from vehicle_routing_problem.parser.demand_parser import parse_cities_demand
from vehicle_routing_problem.parser.graph_parser import parse_graph
from vehicle_routing_problem.reproduction import reproduce
from vehicle_routing_problem.selection import select_individual, select_parents

from vehicle_routing_problem.logger import log


def solve():
    starting_city = "Kraków"
    cars_count = 5
    car_capacity = 1_000
    population_size = 100
    cities_demand = parse_cities_demand("resources/cities_demand.txt")
    cities = [city for city in cities_demand.keys()]
    total_demand = sum(cities_demand.values())

    cities_graph = parse_graph("resources/cities_matrix.xlsx", cities=31)

    current_best_fitness = 0
    distance = 0
    demand = 0

    populations_limit = 1_000

    population = create_initial_population(
        cities=cities,
        cars_count=cars_count,
        population_size=population_size,
    )

    for population_count in range(0, populations_limit):
        individuals_with_fitness = [
            (
                individual,
                fitness(
                    individual=individual,
                    starting_city=starting_city,
                    cars_count=cars_count,
                    car_capacity=car_capacity,
                    cities_demand=cities_demand,
                    cities_graph=cities_graph
                )
            ) for individual in population
        ]

        individuals_with_fitness_value = [
            (individual, fitness[0]) for (individual, fitness) in individuals_with_fitness
        ]

        (best_fitness, best_distance, best_demand) = max(
            individuals_with_fitness, key=lambda x: x[1][0]
        )[1]  # TODO refactor, that's a bit cryptic

        log(
            f'''
            population = {population_count},
            best_fitness = {best_fitness},
            best_distance = {best_distance},
            best_demand = {best_demand}
            '''
        )

        if best_fitness > current_best_fitness:
            current_best_fitness = best_fitness
            distance = best_distance
            demand = best_demand

        number_of_reproductions = int(population_size * 0.8)
        number_of_mutations = population_size - number_of_reproductions

        parents = [select_parents(individuals_with_fitness_value)
                   for _ in range(0, number_of_reproductions)]

        reproduction_products = [
            reproduce(parent1, parent2) for (parent1, parent2) in parents]

        mutation_products = [mutate(select_individual(
            individuals_with_fitness_value), cars_count) for _ in range(0, number_of_mutations)]

        population = reproduction_products + mutation_products

    log(
        f'''
            after all populations:
            best_fitness = {current_best_fitness},
            best_distance = {distance},
            best_demand = {demand}
            total_demand = {total_demand}
            '''
    )
