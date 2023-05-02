# Observable variables

Se trata de variables, las cuales pueden almacenar diferentes tipos de datos, pero que tinen la característica de que otros agentes dentro de la aplicación pueden ser avisados cuando el valor de la variable haya cambiado.

Se trata de variables tipadas, con lo que hay que saber qué tipo de dato va a almacenarse en ella antes de instanciarla, y nunca podrá ser cambiado dicho tipo de dato. Los diferentes tipos de datos son:

- BooleanVar
- DoubleVar
- IntVar
- StringVar

1. Instanciar la variable usando su constructor.
2. Establecer un valor (del tipo de dato correcto) usando el método `set(value)`.
3. Obtener el valor (se retornará con el mismo tipo de dato) usando el método `get()`.

```python
import tkinter as tk

int_var = tk.IntVar()
int_var.set(100)
int_var.get()
```

## Observables

Es posible agregar observables a la variable, para que lance una función (similar a un callback) y así realizar una acción deseada.

Se pueden agregar tantos observables a una misma variable como se quiera.

El observable se crea usando el método `trace()` sobre la variable a la que se quiere agregar dicho observable. Dicho método espera la acción que lanzará la función, y la función en sí.

```python
def my_func(id, ix, act):
    """
    id: identificador interno del observable (no se usará)
    ix: string vacío (gestión interna de tkinter)
    act: "r", "w" o "u"
    """
    pass

int_var.trace("r", my_func)
```

El primer parámetro, la acción que invocará la función, puede ser:

- "r" -> cuando la variable haya sido leída.
- "w" -> cuando se haya modificado su valor.
- "u" -> cuando se haya eliminado.
