# Posicionar widgets en el interior de una ventana

Existen tres métodos (tres managers) diferentes para indicar la posición del widget:

## place()

Se trata del método más detallado. Permite indicar la posición exacta por coordenadas indicadas en píxeles. Sin embargo, tkinter no tratará nunca de "ayudar" para evitar que ciertos widgets se superpongan o cualquier otro error ocurrido por una mala posición indicada.

Argumentos:

- height: altura expresada en píxeles.
- width: ancho expresado en píxeles.
- x: coordenadas horizontal expresada en píxeles de forma relativa a la esquina superior izquierda.
- y: coordenadas vertical expresada en píxeles de forma relativa a la esquina superior izquierda.

## pack()

El desarrollador no se debe preocupar tanto donde posisionar los widgets, en este caso tkinter tratará de buscar la mejor ubicación, aunque el resultado no siempre será el esperado.

Los argumentos a usar en este método están más orientados a como decirle de manera general que tkinter ordene los widgets que se vayan agregando.

- side: fuerza al manager a seguir una dirección al agregar los widgets.
  - TOP: por defecto.
  - BOTTOM
  - LEFT
  - RIGHT
- fill: se indica al manager como expander el widget.
  - NONE: por defecto.
  - X
  - Y
  - BOTH

## grid()

Es una mezcla de los dos anteriores. Permite al desarrollador indicar su deseo general de donde establecer los widgets, aunque con la ayuda de tkinter para evitar problemas de diseño.

Argumentos:

- column: nº de columna donde ubicar el widget. Comienza por 0.
- row: nº de fila donde ubicar el widget. Comienza por 0.
- columnspan
- rowspan

La venta está dividida en nueve celdas, tres filas y tres columnas.

---

Sea como sea, en ningún concepto se pueden mezclar los managers anteriormente indicados en una aplicación con tkinter.

