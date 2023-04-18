# PEP (Python Enhancement Proposals)

Existen tres tipos diferentes de PEPs:

- **Standard tracks**: describe nuevas características e implementaciones del lenguaje.
- **Informational**: describe problemas de diseño, y además información y guías de estilo para la comunidad.
- **Process**: describe diferentes procesos a resolver alrededor de Python.

## ¿Qué define el PEP1?

- **Python's Steering Council**. Un comité de cinco personas quienes se encargan de aceptar o rechazar PEPs.
- **Python's Core Developers**. Grupo de voluntarios que se encargan de gestionar Python.
- **Python's BDFL**. Guido van Rossum, creador original de Python. **B**enevolent **D**ictator **F**or **L**ife.

## ¿Qué define el PEP20 (Zen of Python)?

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

## ¿Qué define el PEP8?

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
