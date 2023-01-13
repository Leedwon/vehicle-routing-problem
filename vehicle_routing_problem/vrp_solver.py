from vehicle_routing_problem.fitness_calculator import fitness


from vehicle_routing_problem.initial_population_factory import create_initial_population
from vehicle_routing_problem.parser.demand_parser import parse_cities_demand
from vehicle_routing_problem.parser.graph_parser import parse_graph
from vehicle_routing_problem.parents_selector import select_parents

from vehicle_routing_problem.logger import log


def solve():
    starting_city = "Kraków"
    cars_count = 5
    car_capacity = 1_000
    population_size = 25
    cities_demand = parse_cities_demand("resources/cities_demand.txt")
    cities = [city for city in cities_demand.keys()]

    cities_graph = parse_graph("resources/cities_matrix.xlsx", cities=31)

    population = create_initial_population(
        cities=cities,
        cars_count=cars_count,
        population_size=population_size,
    )

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

    parents = select_parents(individuals_with_fitness)
    