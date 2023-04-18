class MyMeta(type):
    def __new__(mcs, name, bases, dictionary):
        """_summary_

        Args:
            mcs (MyMeta): class name, just a convention.
            name (str): new class name.
            bases (tuple): base classes tuple.
            dictionary (dict): attributes for new clase.

        Returns:
            MyMeta
        """
        obj = super().__new__(mcs, name, bases, dictionary)
        print(mcs)
        print(type(name))
        print(bases)
        print(dictionary)
        print(type(obj))
        obj.custom_attribute = "Added by My_Meta"
        return obj


class MyObject(metaclass=MyMeta):
    pass


print(MyObject.__dict__)
