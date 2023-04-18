class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError("Crew is incomplete") from e
        # raise RocketNotReadyError("Crew is incomplete")

crew = ["John", "Mary", "Mike"]
print("Final check procedure")

personnel_check()
