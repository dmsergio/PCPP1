# Gestionar eventos

## Buttons

El widget Button tiene la propiedad `command`, al cual se le puede pasar un callback para que realice una acción específica.

```python
import tkinter as tk


def my_callback():
    tk.messagebox.showinfo("Info", "Custom message")

app = tk.Tk()
button = tk.Button(app, text="Button", command=my_callback)
button.pack()
app.mainloop()
```

## Widgets no clickables

El resto de widgets no clickables, como puede ser un label, o un frame, no tienen el atributo `command` ni tampoco se le puede pasar un callback en su constructor.

En lugar de ello, es posible usar el método `bind()`, al cual se le pasa un evento y el callback que se quiere que se ejecute.

El callback (la función que queremos que sea ejecutada) debe esperar obligatoriamente un argumento, el cual será el evento en cuestión. Es posible reutilizar un callback para un widget que admite un comando, que para otro que se pasa a través del evento.

```python
def my_callback(event=None):
    # event será None cuando se invoque desde un widget clickable, es decir, se pase el callback al argumento command
    # event será un objeto de la clase tkinter.Event cuando se invoque el callback a través de un evento
    pass
```

A la hora de establecer un un callback sobre un widget en concreto, se debe pasar por parámetro el evento que queremos que lance el callback, y el callback en cuestión.

```python
def my_callback(event=None):
    pass

label = tk.Label(app, text="My label")
label.bind("<Button-1>", my_callback)
```

Los eventos son pasados con el string del evento en cuestión.

## Vincular y desvincular eventos a un widget

Igual que se puede vincular un evento con un widget, usando el método `bind(event, callback), también es posible desvincularlo en cualquier momento.

Los widgets clickables, como los botones, como disponen de la propiedad `command`, dicha propiedad puede ser modificada en cualquier momento con el método `config`.

```python
# se crea el widget indicándole un callback que será invocado cuando se haga
# click sobre el botón
button = tk.Button(window, "My button", command=my_callback)

# con el método config es posible alterar la propiedad de un widget. En este
# se le está pasando una función que literalmente no hace nada
button.config(command=lambda: None)
```

Para los widgets no clickables, igual que existe el método `bind` para vincular el widget con un evento y callback, existe también el método `unbind` para desvincular el evento en sí.

```python
label = tk.Label(app, text="My label")
label.bind("<Button-1>", my_callback)  # se vincula el evento al widget
label.unbind("<Button-1>")  # se desvincula el evento
```

También se pueden vincular o desvincular eventos a todos los widgets contenidos dentro de una ventana.

```python
window = tk.Tk()
button = ...
label = ...
frame = ...
button.pack()
label.pack()
frame.pack()
window.bind_all("<Button-1>", my_callback)
window.unbind_all("<Button-1>")
```
