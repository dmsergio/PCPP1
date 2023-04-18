from typing import Callable


def my_decorator(function) -> Callable:
    print(f"We are about to call \"{function.__name__}()\"")
    return function


@my_decorator
def greeting() -> None:
    print("Hello everyone!")


if __name__ == "__main__":
    greeting()
