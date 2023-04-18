from enum import Enum


class FuelType(str, Enum):
    ELECTRIC = "electric"
    PETROL = "petrol"


class EngineState(str, Enum):
    ON = "on"
    OFF = "off"


class Engine:
    def __init__(self, fuel_type: FuelType) -> None:
        self.fuel_type = fuel_type
        self.__state = EngineState.OFF

    def __str__(self) -> str:
        return f"{self.__class__.__name__}<{self.fuel_type}>"

    def start(self) -> None:
        print("Engine on!")
        self.__state = EngineState.ON

    def stop(self) -> None:
        print("Engine off!")
        self.__state = EngineState.OFF

    def get_state(self) -> str:
        return self.__state
