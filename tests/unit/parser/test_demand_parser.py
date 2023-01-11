import pytest

from vehicle_routing_problem.parser.demand_parser import parse_cities_demand


@pytest.fixture
def filename() -> str:
    return "tests/resources/cities_demand_test.txt"


def test_parsing_cities_demand(filename: str):
    actual = parse_cities_demand(filename)

    assert actual == {
        "Białystok": 500,
        "Bielsko-Biała": 50,
        "Chrzanów": 400,
        "Gdańsk": 200,
    }
