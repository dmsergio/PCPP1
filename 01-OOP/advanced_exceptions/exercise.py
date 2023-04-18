"""
Try to extend the check list script to handle more different checks, all
reported as RocketNotReady exceptions.

Add your own checks for: batteries and circuits.
"""
import traceback


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


def fuel_check():
    try:
        print(f"Fuel tank is full in {100 / 0}%")
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Problem with fuel gauge") from e

def batteries_check():
    battery_levels = dict(level_1=True, level_2=True)
    try:
        battery_levels["level_1"] is True
        battery_levels["level_2"] is True
        battery_levels["level_3"] is True
    except KeyError as e:
        raise RocketNotReadyError("Problem with the battery levels") from e

def circuits_check():
    # add your own implementation
    pass


crew = ["John", "Mary", "Mike"]
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print(f"RocketNotReady exception: '{f}', caused by '{f.__cause__}'")
        error_details = traceback.format_tb(f.__traceback__)
        print("\n".join(error_details))
        print(traceback.format_exc())
