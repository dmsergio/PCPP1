class Car:
    def __init__(self, vin: str) -> None:
        self.vin = vin
        self.brand = None

    @classmethod
    def init_with_brand(cls, vin: str, brand: str):
        car_ = cls(vin)
        car_.brand = brand
        return car_


if __name__ == "__main__":
    car = Car("abc123")
    another_car = Car.init_with_brand("aaa111", "audi")

    print("First car", car.vin, car.brand)
    print("Second car", another_car.vin, another_car.brand)
