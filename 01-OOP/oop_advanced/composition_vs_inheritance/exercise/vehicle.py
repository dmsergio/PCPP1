from engine import Engine
from tire import Tire


class Vehicle:
    def __init__(self, vin: str, engine: Engine, tires: set[Tire]) -> None:
        self.vin = vin
        self.engine = engine
        self.tires = tires

    def __str__(self) -> str:
        return f"{self.__class__.__name__}<{self.vin}>"
