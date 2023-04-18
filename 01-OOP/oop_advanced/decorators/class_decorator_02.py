# works like function decorator define in decorator_04.py file


class WarehouseDecorator:
    def __init__(self, material, exec):
        self.material = material
        self.exec = exec

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print(
                f"<strong>*</strong> Wrapping items from "
                f"{own_function.__name__} with {self.material} and "
                f"{self.exec}"
            )
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


@WarehouseDecorator("kraft", True)
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator("foil", True)
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator("cardboard", False)
def pack_fruits(*args):
    print("We'll pack fruits:", args)


if __name__ == "__main__":
    pack_books("Alice in Wonderland", "Winnie the Pooh")
    pack_toys("doll", "car")
    pack_fruits("plum", "pear")
