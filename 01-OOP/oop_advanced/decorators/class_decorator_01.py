class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print(f"{self.func.__name__} was called with the following arguments")
        print(f"\targs={args}\n\tkwargs={kwargs}\n")
        self.func(*args, **kwargs)
        print("Decorator is still operating")


@SimpleDecorator
def combiner(*args, **kwargs):
    print(
        "\tHello from the decorated function; received arguments:",
        args,
        kwargs,
    )


if __name__ == "__main__":
    combiner("a", "b", exec="yes")
