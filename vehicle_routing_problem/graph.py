class Graph():
    """
    Class used to represent graph of cities.

    Attributes
    ----------
    adj_matrix : dict
        Adjacency matrix that represents routes between cities i.e:
        {
            'Krakow': {'Warszawa':123},
            'Warszawa': {'Krakow':123},
        }
    """

    def __init__(self):
        self.adj_matrix: dict = {}

    def add_edge(self, city1: str, city2: str, distance: float):
        if city1 not in self.adj_matrix:
            self.adj_matrix[city1] = {}
        if city2 not in self.adj_matrix:
            self.adj_matrix[city2] = {}

        self.adj_matrix[city1][city2] = distance
        self.adj_matrix[city2][city1] = distance

    def distance(self, from_city: str, to_city: str) -> float:
        return self.adj_matrix[from_city][to_city]