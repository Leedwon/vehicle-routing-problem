def parse_cities_demand(filename: str) -> dict:
    cities_to_demand = {}
    with open(filename, encoding="utf8") as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            (city, demand) = line.split(",")
            cities_to_demand[city] = int(demand)

    return cities_to_demand
