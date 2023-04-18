def greeting():
    print("Hello everyone!")


def sample_decorator(function):
    print(f"We are about to call \"{function.__name__}()\"")
    return function


if __name__ == "__main__":
    the_decorator = sample_decorator(greeting)
    the_decorator()
