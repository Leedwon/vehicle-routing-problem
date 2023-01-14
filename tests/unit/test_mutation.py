import random
import pytest

from vehicle_routing_problem.mutation import mutate


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
def cars_count():
    return 5

@pytest.fixture
def mutation_probability():
    return 0.2

@pytest.fixture
def individual():
    return [1.45, 3.17, 4.19, 2.56]

@pytest.fixture
def child():
    return [0.8474337369372327, 3.17, 4.19, 2.56]

def test_mutation(
    seed,
    cars_count,
    mutation_probability,
    individual,
    child
):
    random.seed(seed)

    assert child == mutate(individual, cars_count, mutation_probability)