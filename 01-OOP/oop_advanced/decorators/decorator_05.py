def outer_decorator():
    print("Outer decorator: starting main decorator")
    def wrapper(function):
        print("Outer decorator: starting wrapper")
        def internal_wrapper(*args):
            print("Outer decorator: starting internal_wrapper")
            print(f"Outer decorator: calling {function.__name__} function")
            function(*args)
            print(f"Outer decorator: {function.__name__} finished")
            print()
        return internal_wrapper
    return wrapper


def inner_decorator():
    print("Inner decorator: starting main decorator")
    def wrapper(function):
        print("Inner decorator: starting wrapper")
        def internal_wrapper(*args):
            print("Inner decorator: starting internal_wrapper")
            print(f"Inner decorator: calling {function.__name__} function")
            function(*args)
            print(f"Inner decorator: {function.__name__} finished")
        return internal_wrapper
    return wrapper


@outer_decorator()
@inner_decorator()
def my_function(*args):
    print("Hello from my_function")


if __name__ == "__main__":
    my_function()
