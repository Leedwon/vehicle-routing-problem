import random
from vehicle_routing_problem.util import random_order_and_vehicle


def mutate(
    individual: list,
    cars_count: int,
    mutation_probability: float = 0.1
):
    child = []

    for gene in individual:
        if random.random() < mutation_probability:
            child.append(random_order_and_vehicle(cars_count))
        else:
            child.append(gene)

    return child
