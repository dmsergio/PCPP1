class First:
    def greeting(self) -> str:
        return "Hello from First class"


class Second(First):
    def greeting(self) -> str:
        return "Hello from Second class"


class Third(First):
    def greeting(self) -> str:
        return "Hello from Third class"


class Fourth(Second, Third):
    pass


if __name__ == "__main__":
    assert Fourth().greeting() == "Hello from Second class"
    print("Inheritance classes order for Fourth class:")
    for idx, cls in enumerate(Fourth.__mro__, 1):
        print(" " * 4, idx, cls)
    print("Order in inheritance matters!")
