import random
import pytest

from vehicle_routing_problem.selection import select_individual, select_parents


@pytest.fixture
def seed():
    """
    RNG for this seed produces:
    0.13436424411240122,
    0.8474337369372327,
    0.763774618976614,
    0.2550690257394217,
    0.49543508709194095,
    0.4494910647887381
    """
    return 1


@pytest.fixture
def parent1():
    return [1.23, 3.45, 2.27]


@pytest.fixture
def parent2():
    return [2.43, 3.12, 4.12]

@pytest.fixture
def individuals_with_fitness(parent1, parent2):
    return [
        (parent1, 0.87),
        (parent2, 0.72)
    ]


def test_individual_selection(
    seed,
    individuals_with_fitness,
    parent1
):
    random.seed(seed)

    assert parent1 == select_individual(individuals_with_fitness)

def test_parents_selection(
    seed,
    individuals_with_fitness,
    parent1,
    parent2
):
    random.seed(seed)

    assert (parent1, parent2) == select_parents(individuals_with_fitness)