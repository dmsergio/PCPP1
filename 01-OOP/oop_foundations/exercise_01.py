"""
- create a class representing a mobile phone;
- your class should implement the following methods:
    - __init__ expects a number to be passed as an argument; this method stores
    the number in an instance variable self.number
    - turn_on() should return the message 'mobile phone {number} is turned on'.
    Curly brackets are used to mark the place to insert the object's number
    variable;
    - turn_off() should return the message 'mobile phone is turned off';
    - call(number) should return the message 'calling {number}'. Curly brackets
    are used to mark the place to insert the object's number variable;
"""

class PhoneMobile:
    def __init__(self, number: str) -> None:
        self.number = number

    def turn_on(self) -> str:
        return f"mobile phone {self.number} is turned on"

    def turn_off(self) -> str:
        return "mobile phone is turned off"

    def call(self, number: str) -> str:
        return f"calling {number}"


def get_random_phone_number() -> str:
    import random
    number = int(random.random() * 100_000)
    number_str = str(number).zfill(5)
    return f"0034-{number_str}"


if __name__ == "__main__":
    phone_a = PhoneMobile(get_random_phone_number())
    phone_b = PhoneMobile(get_random_phone_number())
    print(phone_a.turn_on())
    print(phone_b.turn_on())
    print(phone_b.call("993332211"))
    print(phone_a.call("994448877"))
    print(phone_a.turn_off())
    print(phone_b.turn_off())
