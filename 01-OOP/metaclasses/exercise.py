"""
- Imagine you’ve been given a task to clean up the code of a system developed
  in Python – the code should be treated as legacy code;
- The system was created by a group of volunteers who worked with no clear
  “clean coding” rules;
- The system suffers from a problem: we don’t know in which order the classes
  are created, so it causes multiple dependency problems;
- Your task is to prepare a metaclass that is responsible for:
    - equipping all newly instantiated classes with time stamps, persisted in a
      class attribute named instantiation_time;
    - equipping all newly instantiated classes with the
      get_instantiation_time() method. The method should return the value of
      the class attribute instantiation_time.
"""


def get_instantiation_time(self):
    return self.instantiation_time


class TimestampMeta(type):
    def __new__(mcs, name, bases, dictionary):
        if "instantiation_time" not in dictionary:
            dictionary["instantiation_time"] = None
        if "get_instantiation_time" not in dictionary:
            dictionary["get_instantiation_time"] = get_instantiation_time
        return super().__new__(mcs, name, bases, dictionary)


class BaseClass(metaclass=TimestampMeta):
    pass
