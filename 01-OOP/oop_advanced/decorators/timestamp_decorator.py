from datetime import datetime
import math
import time


def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def timestamp_log():
    def wrapper(function):
        def internal_wrapper(*args):
            print(f"{function.__name__} started at: {get_current_time()}")
            print(function(*args))
            print(f"{function.__name__} finished at: {get_current_time()}")
            print()
        return internal_wrapper
    return wrapper


@timestamp_log()
def multiply(*args, **kwargs):
    time.sleep(1)
    return math.prod(args)


if __name__ == "__main__":
    multiply(1, 2, 3, 4, 5)
    multiply(900000000000, 78072348957423095872394857, 97123490871249871342907)
