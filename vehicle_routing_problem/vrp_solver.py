from vehicle_routing_problem.fitness_calculator import fitness


from vehicle_routing_problem.initial_population_factory import create_random_routes
from vehicle_routing_problem.parser.demand_parser import parse_cities_demand
from vehicle_routing_problem.parser.graph_parser import parse_graph


def solve():
    starting_city = "Kraków"
    cars_count = 5
    car_capacity = 1_000
    cities_demand = parse_cities_demand("resources/cities_demand.txt")

    total_demand = sum(cities_demand.values())

    cities_graph = parse_graph("resources/cities_matrix.xlsx", cities=31)

    individual = create_random_routes(
        cities=cities_demand.keys(),
        cars_count=cars_count
    )

    fitness(
        individual=individual,
        starting_city=starting_city,
        cars_count=cars_count,
        car_capacity=car_capacity,
        cities_demand=cities_demand,
        cities_graph=cities_graph
    )
