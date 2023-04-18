import abc


class Person(abc.ABC):

    @abc.abstractmethod
    def hello(self):
        pass


class Child(Person):

    def hello(self):
        print("Hey there!")


class Senior(Person):

    def greeting(self):
        print("Hello!")


if __name__ == "__main__":
    child = Child()
    child.hello()

    senior = Senior()
    senior.greeting()
