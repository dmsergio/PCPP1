# Propiedades de los widgets

## Acceder a las propiedades

### Usando un diccionario

Es posible acceder y modificar a cada una de las propiedades de un widget como si de un diccionario se tratara.

```python
button = tk.Button(widget, text="My button", command=my_callback)
button["text"] = "Hey!"
```

### cget y config

`cget` se usará para obtener el valor de una propiedad.
`config` se usará para establecer un nuevo valor a una propiedad.

## Estilo de fuente

EL nombre de la propiedad es `font`.

Los valores se deben especificar mediante tuplas, con el siguiente formato:

```python
# font = ("font_family_name", "font_size", "font_style")
label_1 = tk.Label(window, text="My custom text", font=("Times", "12"))
label_2 = tk.Label(window, text="My custom text", font=("Arial", "16", "bold"))
```
