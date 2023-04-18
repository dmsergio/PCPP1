def hello(self) -> str:
    return "Hello"

Dog = type("Dog", (list,), {"hello": hello})
dog = Dog()

print("The class name is:", Dog.__name__)
print("The class is an instance of:", Dog.__class__)
print("The class is based on:", Dog.__bases__)
print("The class attributes are:", Dog.__dict__)

print(dog.hello())
