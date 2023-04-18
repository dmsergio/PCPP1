class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError("The value must to be integer type!")

    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        # list.__setitem__(self, index, value)
        return super().__setitem__(index, value)

    def append(self, value) -> None:
        IntegerList.check_value_type(value)
        # list.append(self, value)
        return super().append(value)

    def extend(self, iterable) -> None:
        for value in iterable:
            IntegerList.check_value_type(value)
        # list.extend(self, iterable)
        return super().extend(iterable)
