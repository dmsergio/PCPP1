"""
Imagine that you receive a task description of an application that monitors the
process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot
exceed 300 units.

Write a code that creates objects representing apples as long as both
limitations are met. When any limitation is exceeded, than the packaging
process is stopped, and your application should print the number of apple
class objects created, and the total weight.

Your application should keep track of two parameters:

    - the number of apples processed, stored as a class variable;
    - the total weight of the apples processed; stored as a class variable.
    Assume that each apple's weight is random, and can vary between 0.2 and 0.5
    of an imaginary weight unit;

Hint: Use a random.uniform(lower, upper) function to create a random number
between the lower and upper float values.
"""
import random


class Apple:
    def __init__(self, weight) -> None:
        self.weight = weight


class Packaging:
    LIMIT_WEIGHT = 300
    apples_count = 0
    total_weight = 0.0

    def __init__(self, weight) -> None:
        self.weight = weight
        Packaging.apples_count += 1
        Packaging.total_weight += self.weight

    @classmethod
    def are_space_available(cls, apple: Apple) -> bool:
        return cls.total_weight + apple.weight <= cls.LIMIT_WEIGHT


def get_apple_weight() -> float:
    return random.uniform(0.2, 0.5)


def main() -> None:
    print("*" * 55)
    print("*" * 8, "Apples Packaging process has started!", "*" * 8)
    print("*" * 55)

    for _ in range(1_000):
        apple = Apple(weight=get_apple_weight())
        if not Packaging.are_space_available(apple):
            break
        Packaging(apple.weight)

    print("Total apples packaged:", Packaging.apples_count, "uds.", sep=" ")
    print("Total package weight:", Packaging.total_weight, "kg.", sep=" ")


if __name__ == "__main__":
    main()
