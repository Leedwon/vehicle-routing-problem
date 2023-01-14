import random
import pytest

from vehicle_routing_problem.reproduction import reproduce


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
    return [1.23, 3.43, 5.12, 2.87]


@pytest.fixture
def parent2():
    return [1.44, 1.78, 4.12, 3, 34]


@pytest.fixture
def child():
    return [1.23, 1.78, 4.12, 2.87]


def test_reproduction(
    seed,
    parent1,
    parent2,
    child
):
    random.seed(seed)

    assert child == reproduce(parent1, parent2)
