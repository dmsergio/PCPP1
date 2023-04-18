class Tire:
    def __init__(self, size: int) -> None:
        self.size = size
        self.__pressure = 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__}<{self.size}>"

    def get_pressure(self) -> int:
        return self.__pressure

    def pump(self) -> None:
        print("Tire pressure filled!")
        self.__pressure = 100
