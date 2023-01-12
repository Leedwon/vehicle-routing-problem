import random


from vehicle_routing_problem.graph import Graph
from vehicle_routing_problem.parser.demand_parser import parse_cities_demand
from vehicle_routing_problem.parser.graph_parser import parse_graph

LOGGING_ENABLED = True


def log(msg: str):
    if (LOGGING_ENABLED):
        print(msg)


def fitness(
    individual: list,
    starting_city: str,
    cars_count: int,
    car_capacity: int,
    cities_demand: dict,
    cities_graph: Graph,
) -> float:
    cities = [city for city in cities_demand.keys()]

    car_routes = extract_rotues_for_cars(
        starting_city=starting_city,
        individual=individual,
        cars_count=cars_count,
        cities=cities
    )

    demand_satisfied = calculate_demand(
        routes=car_routes,
        car_capacity=car_capacity,
        cities_demand=cities_demand
    )

    log(f'demand_satisfied = {demand_satisfied}')

    pass


def calculate_demand(
    routes: list,
    car_capacity: int,
    cities_demand: dict
) -> int:
    cars_capacities = [car_capacity for car in range(0, len(routes))]

    visited_cities = set()

    total_demand = 0

    for index, route in enumerate(routes):
        for city in route[1:]:  # omitting initial_city as it has no demand
            # don't add demand if city was already visited
            # each city should be visited only once - visiting it twice can be a caused by infeasible reproduction
            # this will penalize such cases
            if city not in visited_cities:
                demand = cities_demand[city]
                if cars_capacities[index] >= demand:
                    cars_capacities[index] -= demand
                    total_demand += demand
                    visited_cities.add(city)

    return total_demand


def extract_rotues_for_cars(
    individual: list,
    starting_city: str,
    cars_count: int,
    cities: list,
) -> list:
    car_routes = [[starting_city] for _ in range(0, cars_count)]

    cities_to_keys = [(cities[i], key) for i, key in enumerate(individual)]

    sorted_cities_to_keys = sorted(
        cities_to_keys, key=lambda item: item[1] % 1)

    for city, key in sorted_cities_to_keys:
        car_index = int(key)
        car_routes[car_index].append(city)

    return car_routes


def create_initial_population(
    cities: list,
    cars_count: int,
    population_size: int = 25,
):
    return [create_random_routes(cities, cars_count) for _ in range(0, population_size)]


def create_random_routes(
    cities: list,
    cars_count: int,
) -> list:
    return [random_order_and_vehicle(cars_count) for _ in cities]


def random_order_and_vehicle(cars_count: int) -> float:
    """generate random order and vehicle encoded as random key integer part represents car index and fractional part represents order"""
    return random.random() + random.randint(0, cars_count - 1)


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
