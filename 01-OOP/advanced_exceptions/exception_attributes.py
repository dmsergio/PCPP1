from pprint import pprint


def print_attributes(exception: BaseException):
    print(type(exception))
    pprint(dir(exception))
    print()


try:
    import unknown_module
except BaseException as e:
    print_attributes(e)

try:
    int("a")
except BaseException as e:
    print_attributes(e)

try:
    [][0]
except BaseException as e:
    print_attributes(e)
