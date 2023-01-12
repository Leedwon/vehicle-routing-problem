import random


def fitness(
    individual: list,
    starting_city: str,
    cars_count: int,
    cities: list
) -> float:
    car_routes = extract_rotues_for_cars(
        starting_city=starting_city,
        individual=individual,
        cars_count=cars_count,
        cities=cities
    )

    # TODO car routes are ready now calculate fitness
    pass


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
