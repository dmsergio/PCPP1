class GasEngine:
    def __init__(self, horse_power) -> None:
        self.hp = horse_power

    def start(self):
        print(f"Starting {self.hp}hp gas engine")


class DieselEngine:
    def __init__(self, horse_power) -> None:
        self.hp = horse_power

    def start(self):
        print(f"Starting {self.hp}hp diesel engine")


class Car:
    def __init__(self, engine: GasEngine | DieselEngine) -> None:
        self.engine = engine


if __name__ == "__main__":
    car = Car(GasEngine(2000))
    car.engine.start()
    car.engine = DieselEngine(2500)
    car.engine.start()
