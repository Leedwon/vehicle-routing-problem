import pytest

from vehicle_routing_problem.graph import Graph


@pytest.fixture
def graph() -> Graph:
    return Graph()


def test_adding_edge(graph: Graph):
    graph.add_edge("Krakow", "Warszawa", 123)
    assert graph.adj_matrix == {
        'Krakow': {'Warszawa': 123},
        'Warszawa': {'Krakow': 123},
    }
