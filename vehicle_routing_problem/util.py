import random


def random_order_and_vehicle(cars_count: int) -> float:
    """generate random order and vehicle encoded as random key integer part represents car index and fractional part represents order"""
    return random.random() + random.randint(0, cars_count - 1)
