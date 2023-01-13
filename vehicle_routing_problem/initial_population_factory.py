from vehicle_routing_problem.util import random_order_and_vehicle


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
