from vehicle_routing_problem.graph import Graph

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

    total_demand = sum(cities_demand.values())

    distance = calculate_distance(
        routes=car_routes,
        cities_graph=cities_graph
    )

    # total demand is more important than short distance
    penalty = (total_demand - demand_satisfied) * 10

    total = distance + penalty  # TODO adjust parameters
    fitness = 10_000 / total  # since higher is better

    return (fitness, distance, demand_satisfied)


def calculate_distance(routes: list, cities_graph: Graph) -> float:
    sums = [route_distance(route, cities_graph) for route in routes]
    return sum(sums)


def route_distance(route: list, cities_graph: Graph) -> float:
    pairs = zip(route, route[1:])
    distance = 0
    for (from_city, to_city) in pairs:
        addition = cities_graph.distance(from_city, to_city)
        distance += addition
    return distance


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
