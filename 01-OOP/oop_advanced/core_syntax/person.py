class Person:
    def __init__(self, name: str, age: int, weight: float) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def __add__(self, other) -> float:
        return self.weight + other.weight
