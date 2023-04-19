# PEP (Python Enhancement Proposals)

Existen tres tipos diferentes de PEPs:

- **Standard tracks**: describe nuevas características e implementaciones del lenguaje.
- **Informational**: describe problemas de diseño, y además información y guías de estilo para la comunidad.
- **Process**: describe diferentes procesos a resolver alrededor de Python.

## PEP1

- **Python's Steering Council**. Un comité de cinco personas quienes se encargan de aceptar o rechazar PEPs.
- **Python's Core Developers**. Grupo de voluntarios que se encargan de gestionar Python.
- **Python's BDFL**. Guido van Rossum, creador original de Python. **B**enevolent **D**ictator **F**or **L**ife.

## PEP20 (Zen of Python)

Colección de 19 sentencias que reflejan la filosofía detrás de Python, sus principios, y el diseño. Este "poema" fue escrito por Tim Peters.

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

## PEP8

Describe las convenciones para programar en Python. Se trata de una serie de guías de estilo que se deben seguir en la implementación de proyectos. Aún así, no se trata de una guía de estilos estricta, sino más bien una guía que se debería seguir siempre y cuando sea posible.

La idea principal de este PEP es la de ofrecer unas convenciones para ser consistente a la hora de programar, aún siendo totalemente elegible adoptar unas convenciones propias, pero siempre siendo consistentes con ellas.

### Herramientas para comprobar el estilo del código

- **pycodestyle**. Comprueba el estilo del código.

    `pip install pycodestyle`

- **autopep8**. Formatea el código en base al resultado de la herramienta "pycodestyle".

    `pip install autopep8`

- [**PEP 8 online**](http://pep8online.com/about). Herramienta online.

### Recomendaciones

**Indentación**

- Usar cuatro espacios para identar.
- Usar espacios en lugar de tabulaciones.
- En Python 3 no está permitido identar con espacios y con tabulaciones. Se debe escoger uno de ellos. De lo contrario Python lanzará la excepción *TabError*.

**Longitud de línea**

- Máximo de 79 caracteres.
- En comentarios y docstrings, no debe exceder de 72 caracteres.
- Por conveniencia, se puede subir a 99 caracteres (para comentarios y docstrings sigue a 72).

**Importaciones**

- Siempre al principio del fichero.
- Seguir el orden:
    1. Librerías estándar.
    2. Paquetes de terceros.
    3. Librerías propias.
- Una importación por línea.

**Strings**

- PEP8 no especifica si usar comillas simples o dobles a la hora de definir strings. Simplemente escoger la opción deseada y ser constante con ella.

**Comentarios**

- Máximo 72 caracteres por línea.
- Comenzar siempre en mayúscula (a no ser que se trate de un identificador) y terminar la sentencia con un "punto".
- En los bloques de comentarios donde hay más de una línea, se debe separar cada párrafo por una línea en blanco (pero igualmente comentada con el símbolo "#").
- En los comentarios que se indican a la misma altura que una expresión Python, usar dos o más espacios para separar la expresión en sí con el comentario.

**Convención de nombres**

- **Variables**: *snake_case*, ej.: `name`, `last_name`
- **Funciones**: *snake_case*, ej.: `print`, `check_value`
- **Métodos**: *snake_case*, ej.: `exists`, `get_name`
- **Clases**: *CamelCase*, ej.: `Vehicle`, `AirVehicle`
- **Constantes**: *SNAKE_CASE*, ej.: `PI`, `DISCOUNT_VALUE`
- **Módulos**: *snake_case*, ej.: `utils.py`, `math_utils.py`
- **Paquetes**: *lowercase*, ej.: `utils`, `mathutils`
- **Tipos de varialbes**: *CamelCase*, ej.: `Num`, `AnyStr`

**Recomendaciones al programar**

- Hacer comparaciones sobre `None` con los operadores `is` y `is not`.
- Hacer comparaciones sobre valores booleanos con los operadores `is` y `is not`.
- Mejor usar el operador `is not` en lugar de `not ... is`.
- Capturar las excepciones de forma explícita, no simplemente con la sentencia `except:`.

## PEP257

Estandarización para estructurar los docstring. Muestra las convenciones, buenas prácticas, y semánticas. Trata de responder las siguientes questiones:

- ¿Qué debería contener un docstring de Python?
- ¿Cómo debería usarse un docstring de Python?

El docstring es un string de documentación en Python que se usa tanto en clases, módulos, métodos y funciones para agregarles información sobre su finalidad y funcionamiento. El docstring debe ir dentro del objeto a documentar, ej.:

```python
class MyClass:
    """MyClass docstring"""

    @staticmethod
    def my_func():
        """my_func docstring"""
        pass
```

- El docstring debe estar envuelto entre tres comillas dobles; `"""..."""`.
- Comenzar siempre en mayúscula (a no ser que se trate de un identificador) y terminar la sentencia con un "punto".
- Debe ser imperativo.

### Formatos de docstring

**reStructuredText**

- Formato oficial de Python descrito en el PEP287.
    ```python
    def get_full_name(name="Sergio", last_name=""):
        """Returns a full name composed by name + last_name.

        Keyword arguments:
        :arg name: the person name (default: "Sergio")
        :type name: str
        :arg last_name: the person last name (default: "")
        :type name: str
        """
        return f"{name} {last_name}"
    ```

**NumPy/SciPy**

- Combinación entre "Google docstrings" y "reStructuredText".
    ```python
    def get_full_name(name="Sergio", last_name=""):
        """Returns a full name composed by name + last_name.

        Parameters:
        -----------
        name: str
            The person name (default: "Sergio").
        last_name:
            The person last name (default: "").
        """
        return f"{name} {last_name}"
    ```

## Linters y Fixers

**Linters**

- Flake8
- Pylint
- Pyflakes
- Pychecker
- Mypy
- Pycodestyle

**Fixers**

- Black
- YAPF
- autopep8
