class Duck:
    # Las variables de clase son compartidas para cada una de las instancias
    # creadas de la propia clase, y pueden ser accesibles tanto desde la clase
    # como del objeto instanciado. Eso si, únicamente se puede modificar su
    # valor desde la clase, nunca desde la instancia. Intentando esto último lo
    # que se consigue es crear una variable de instancia para dicho objecto con
    # el mismo nombre que la variable de la clase.
    class_var = "Duck class!"

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

def show_properties(objects: list):
    print(Duck.__dict__)
    print(Duck.class_var)
    for obj in objects:
        print(obj.class_var)
        print(
            "All the variables available for the instance '%s': ",
            obj,
            obj.__dict__,
        )


def main():
    duckling = Duck(height=10, weight=3.4, sex="male")
    drake = Duck(height=25, weight=3.7, sex="male")
    hen = Duck(height=20, weight=3.4, sex="female")

    show_properties([duckling, drake, hen])
    duckling.name = "Duckling"
    show_properties([duckling, drake, hen])


if __name__ == "__main__":
    main()
