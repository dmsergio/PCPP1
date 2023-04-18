"""
- Create a class representing a time interval.
- the class should implement its own method for addition, subtraction on time
interval class objects;
- the class should implement its own method for multiplication of time interval
class objects by an integer-type value;
- the __init__ method should be based on keywords to allow accurate and
convenient object initialization, but limit it to hours, minutes, and seconds
parameters;
- the __str__ method should return an HH:MM:SS string, where HH represents
hours, MM represents minutes and SS represents the seconds attributes of the
time interval object;
- check the argument type, and in case of a mismatch, raise a TypeError
exception.
"""
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR


class Time:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:

        def sanitize_value(obj) -> int:
            if isinstance(obj, (float, str)):
                try:
                    return int(obj)
                except TypeError | ValueError:
                    raise TypeError(
                        "Impossible convert %s value to 'int'", obj
                    )
            elif not isinstance(obj, int):
                raise TypeError(
                    "'int' or 'float' arguments are expected, %s is given.",
                    type(obj),
                )
            return obj

        hours = sanitize_value(hours)
        minutes = sanitize_value(minutes)
        seconds = sanitize_value(seconds)

        if not (0 <= seconds < SECONDS_IN_MINUTE):
            raise ValueError("Seconds value must be between 0 and 59!")
        if not (0 <= minutes < MINUTES_IN_HOUR):
            raise ValueError("Minutes value must be between 0 and 59!")

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def _format_result(hours: int, minutes: int, seconds: int) -> str:
        h = str(hours).zfill(2)
        m = str(minutes).zfill(2)
        s = str(seconds).zfill(2)
        return f"{h}:{m}:{s}"

    def __str__(self) -> str:
        return self._format_result(self.hours, self.minutes, self.seconds)

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}>"
                f"(h={self.hours}, m={self.minutes}, s={self.seconds})")

    @staticmethod
    def _convert_to_seconds(
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
    ) -> int:
        if hours:
            seconds += hours * SECONDS_IN_HOUR
        if minutes:
            seconds += minutes * SECONDS_IN_MINUTE
        return seconds

    @staticmethod
    def _seconds_to_datetime_values(seconds: int) -> tuple[int, int, int]:
        hours = seconds // SECONDS_IN_HOUR
        residual_seconds = seconds % SECONDS_IN_HOUR
        minutes = residual_seconds // SECONDS_IN_MINUTE
        seconds = residual_seconds % SECONDS_IN_MINUTE
        return int(hours), int(minutes), int(seconds)

    def __get_total_seconds(self) -> int:
        seconds = self.seconds
        seconds += self.minutes * SECONDS_IN_MINUTE
        seconds += self.hours * SECONDS_IN_HOUR
        return seconds

    @classmethod
    def __get_seconds_from_other(cls, other) -> int:
        if isinstance(other, int):
            seconds = other
        elif isinstance(other, cls):
            seconds = other.__get_total_seconds()
        else:
            raise ValueError(
                f"'int' or '{cls.__name__}' is expected, but "
                f"'{type(other).__name__}' is given!",
            )
        return seconds

    def __add__(self, other) -> str:
        self_total_seconds = self.__get_total_seconds()
        other_total_seconds = self.__class__.__get_seconds_from_other(other)
        seconds = self_total_seconds + other_total_seconds
        return self._format_result(*self._seconds_to_datetime_values(seconds))

    def __sub__(self, other) -> str:
        self_total_seconds = self.__get_total_seconds()
        other_total_seconds = self.__class__.__get_seconds_from_other(other)
        seconds = self_total_seconds - other_total_seconds
        if seconds <= 0:
            return "00:00:00"
        return self._format_result(*self._seconds_to_datetime_values(seconds))

    def __mul__(self, num: int) -> str:
        seconds = self.__get_total_seconds() * num
        if seconds <= 0:
            return "00:00:00"
        return self._format_result(*self._seconds_to_datetime_values(seconds))
