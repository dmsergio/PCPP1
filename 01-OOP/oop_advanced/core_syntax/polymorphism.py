class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Kid(Person):
    pass


class Senior(Person):
    pass


def main() -> None:
    for obj in (
        Kid(name="Peter", age=10),
        Senior(name="Julius", age=55),
    ):
        print(obj.name)
        print(obj.age)


if __name__ == "__main__":
    main()
