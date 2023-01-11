import pytest
from vehicle_routing_problem.parser import graph_parser


@pytest.fixture
def file_path() -> str:
    return "tests/resources/cities_matrix_test.xlsx"


@pytest.fixture
def cities_count() -> int:
    return 4


def test_graph_parser(file_path: str, cities_count: int):
    graph = graph_parser.parse_graph(file_path, cities_count)
    assert graph.adj_matrix == {
        'Białystok': {'Bielsko-Biała': 557, 'Chrzanów': 524, 'Gdańsk': 429},
        'Bielsko-Biała': {'Białystok': 557, 'Chrzanów': 50.4, 'Gdańsk': 587},
        'Chrzanów': {'Białystok': 524, 'Bielsko-Biała': 50.4, 'Gdańsk': 551},
        'Gdańsk': {'Białystok': 429, 'Bielsko-Biała': 587, 'Chrzanów': 551},
    }
