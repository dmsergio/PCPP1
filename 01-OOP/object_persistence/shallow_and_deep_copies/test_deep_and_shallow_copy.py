import copy
import time


if __name__ == "__main__":
    a_list = [(1,2,3) for _ in range(1_000_000)]

    print("Single reference copy")
    time_start = time.time()
    b_list = a_list
    print("Execution time:", round(time.time() - time_start, 3))
    print("Memory chunks:", id(a_list), id(b_list))
    print("Same memory chunk?", a_list is b_list)

    print()

    print("Shallow copy")
    time_start = time.time()
    # b_list = a_list[:]
    b_list = copy.copy(a_list)
    print("Execution time:", round(time.time() - time_start, 3))
    print("Memory chunks:", id(a_list), id(b_list))
    print("Same memory chunk?", a_list is b_list)

    print()

    print("Deep copy")
    time_start = time.time()
    b_list = copy.deepcopy(a_list)
    print("Execution time:", round(time.time() - time_start, 3))
    print("Memory chunks:", id(a_list), id(b_list))
    print("Same memory chunk?", a_list is b_list)
