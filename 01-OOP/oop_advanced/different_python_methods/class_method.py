class MyObject:
    __instantiate_counter = 0

    def __init__(self) -> None:
        MyObject.__instantiate_counter += 1

    @classmethod
    def get_instantiate_counter(cls):
        return f"# of objects created: {cls.__instantiate_counter}"


if __name__ == "__main__":
    print(MyObject.get_instantiate_counter())

    obj_1 = MyObject()
    print(MyObject.get_instantiate_counter())

    obj_2 = MyObject()
    print(MyObject.get_instantiate_counter())
