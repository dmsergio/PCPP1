# Coloreando los widgets

En el momento de instanciar un widget, existen una serie de propiedades para poder establecer ciertos colores.

Es posible indicar los colores usando sus correspondiente palabra en inglés, o la numeración RGB.

## Colores en inglés

Se puede encontrar la lista completa de nombres [aquí](https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html).

## RGB

- R=0;G=0;B=0 -> negro.
- R=255;G=255;B=255 -> blanco.

Para poder usar la codificación RGB y establecer colores en los atributos de los widgets, se usa el formato hexadecimal: `#FFFFFF`.

Cada par de dígitos (00...FF) va de 0 a 255, justo el rango que permite la codificación RGB.

- RGB=0;0;0; es equivalente a #000000
- RGB=255;255;255; es equivalente a #FFFFFF
