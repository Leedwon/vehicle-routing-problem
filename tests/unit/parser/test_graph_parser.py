import pytest
from vehicle_routing_problem.graph import Graph
from vehicle_routing_problem.parser import graph_parser


@pytest.fixture
def file_path() -> str:
    return "tests/resources/cities_matrix_test.xlsx"


@pytest.fixture
def cities_count() -> int:
    return 4


@pytest.fixture
def city() -> str:
    return 'Krakow'


@pytest.fixture
def other_city() -> str:
    return 'Katowice'


@pytest.fixture
def distance() -> float:
    return 123.0


@pytest.fixture
def graph(city: str, other_city: str, distance: float) -> Graph:
    graph = Graph()
    graph.add_edge(city1=city, city2=other_city, distance=distance)
    return graph


def test_graph_parser(file_path: str, cities_count: int):
    graph = graph_parser.parse_graph(file_path, cities_count)
    assert graph.adj_matrix == {
        'Białystok': {'Bielsko-Biała': 557, 'Chrzanów': 524, 'Gdańsk': 429},
        'Bielsko-Biała': {'Białystok': 557, 'Chrzanów': 50.4, 'Gdańsk': 587},
        'Chrzanów': {'Białystok': 524, 'Bielsko-Biała': 50.4, 'Gdańsk': 551},
        'Gdańsk': {'Białystok': 429, 'Bielsko-Biała': 587, 'Chrzanów': 551},
    }


def test_distance_between_cities(city: str, other_city: str, graph: Graph, distance: float):
    actual = graph.distance(from_city=city, to_city=other_city)
    assert actual == distance
