from typing import Callable


def my_decorator(function) -> Callable:

    def internal_wrapper(*args, **kwargs):
        print(
            f"Function \"{function.__name__}()\" has been called with the "
            f"next arguments:"
        )
        print(f"\targs: {args}\n\tkwargs: {kwargs}")
        function(*args, **kwargs)

    return internal_wrapper


@my_decorator
def greeting(*args, **kwargs) -> None:
    print("Hello from decorated function; received arguments:", args, kwargs)


if __name__ == "__main__":
    greeting("a", "b", exec=True)
