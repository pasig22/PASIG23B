# Python
<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="https://keyspatial.com">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Hacé click acá para dejar tu feedback sobre esta clase.
      </a>
    </td>
  </tr>
</table>

#### En esta lección cubriremos:

* Introducción a Python
* Variables
* Strings, Numbers y Booleanos


Python es un lenguaje de programación interpretado, orientado a objetos y de alto nivel. Fue creado por Guido van Rossum en 1991, Python fue idealizado para ser un lenguaje fácil, intuitivo, de código abierto y adecuado para tareas del día a día. Su simplicidad ayuda en la reducción del mantenimiento del código, su soporte a módulos y paquetes fomentan la programación modularizada y reutilización de código.
.

Vamos a aprender los conceptos más básicos de Python:

## Variables

Una variable es una forma de almacenar el valor de algo para usar más tarde. (Una nota para aquellos con conocimientos previos de programación: Python es un lenguaje de tipado dinámico, pues las variables no necesitan ser declaradas especificando su tipo al iniciar la variable.

Se define con la siguiente sintaxis:

** nombreVariable = valor_de_la_variable **

> Nota 1: Las palabras claves o keywords son palabras especiales que utiliza el lenguaje para indicar algo. No podremos usas las palabras claves del lenguaje cómo nombres de variables.
> Nota 2: Utilizar nombres descriptivos y en minúsculas, no rebazar por palabra 10 caractéres.
> Nota 3: Para variables de dos o mas palabras, iniciar la segunda palabra con mayúscula (P.E: cveMun), tambien, cuando sean más de dos palabras utilizar solo tres caractéres.

```javascript
muncipio = 'Jilotepec'
cveMun = '036'
tasPorMun = 2094.90// Tasa porcentual por municipio
```
aqui voy

#### print()

Otro concepto del que hablaremos de inmediato es

```Python
print()
```

Este método muy simple nos permitirá imprimir en la consola todo lo que pongamos entre paréntesis.

## Tipos de Datos

En ciencias de la computación, un tipo de dato informático o simplemente tipo, es un atributo de los datos que indica la clase de datos que se va a manejar. Esto incluye imponer restricciones en los datos, como qué valores pueden tomar y qué operaciones se pueden realizar.

Los tipos de datos aceptados varían de lenguaje en lenguaje.

Los tipos de datos más básicos en Python son ***Strings***, ***Numbers***, and ***Booleans***.

### Strings

Las "strings" son bloques de texto, siempre se definirán entre comillas doble. Cualquier texto entre comillas es una cadena o string.

```Python
nombrePerro = "firulais"
```

### Numbers

Los números son solo eso, números. Los números NO se envuelven en comillas. Pueden ser negativos también. Python tiene una limitación en el tamaño de un número (+/- 9007199254740991), pero muy raramente aparecerá esa limitación en nuestro uso diario.

```Python
positivo = 27
negativo = -40
```

### Boolean

Los booleanos provienen de la [lógica de Boole](https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole). Es un concepto que alimenta el código binario y el núcleo de las computadoras. Es posible que haya visto código binario en el pasado (0001 0110…), esto es lógica booleana. Esencialmente significa que tiene dos opciones, activar o desactivar, 0 o 1, verdadero o falso. En Javascript usamos booleanos para significar verdadero o falso. Esto puede parecer simple al principio, pero puede complicarse más adelante.

```Python
meAgradaPython = true
```

Los valores posibles de un dato booleando en Python son: `true` o `false`.

## Operadores

Vamos a poder realizar operaciones en JavaScript a través de los ***operadores***. Básicamente son símbolos que ya conocemos (`+`, `-`, `/`, `*`) que indican al intérprete de JavaScript las operaciones que debe realizar.

Por ejemplo: Para el intérprete al ver el signo `+`, sabe que tiene que ejecutar la función suma (que tiene internamente definida), y toma como parámetros los términos que estén a la izquierda y la derecha del operador.

```Python
a = 2 + 3 # a = 5
b = 3 / 3 # b = 1
```

## Precedencia de Operadores y Asociatividad

Esto parece aburrido, pero nos va a ayudar a saber cómo piensa el intérprete y bajo qué reglas actúa.

La *precedencia de operadores* es básicamente el orden en que se van a llamar las funciones de los operadores. Estás funciones son llamadas en ***orden de precedencia*** (las que tienen **mayor** precedencia se ejecutan primero).  O sea que si tenemos más de un operador, el intérprete va a llamar al operador de mayor precendencia primero y después va a seguir con los demás.

La *Asociatividad de operadores* es el orden en el que se ejecutan los operadores cuando tienen la misma precedencia, es decir, de izquierda a derecha o de derecha a izquierda.

> Podemos ver la documentación completa sobre Precedencia y Asociatividad de los operadores de Python [acá](https://docs.python.org/es/3/library/operator.html)

Por ejemplo: `print( 3 + 4 * 5)` Para resolver esa expresión y saber qué resultado nos va a mostrar el intérprete deberíamos conocer en qué orden ejecuta las operaciones. Al ver la tabla del link de arriba, vemos que la multiplicación tiene una precedencia de 15, y la suma de 14. Por lo tanto el intérprete primero va a ejecutar la multiplicación y luego la suma con el resultado de lo anterior -> ( 3 + 20 )` -> `print(23)`.

Cuando invocamos una función en Python, los **argumentos** son evaluados primero(se conoce como **non-lazy** evaluation), está definido en la [especificación](http://es5.github.io/#x11.2.3).

No confundir el orden de ejecución con asociatividad y precedencia, [ver esta pregunta de StackOverflow](https://barcelonageeks.com/precedencia-y-asociatividad-de-operadores-en-python/).

Ahora si tuvieramos la misma precedencia entraría en juego la asociatividad, veamos un ejemplo:

```Python
a = 1, b = 2, c = 3

a = b = c

print(a, b, c)
```

Qué veriamos en el print(). Para eso tenemos que revisar la tabla por la asociatividad del operador de asignación `=`. Este tiene una precedencia de 3 y una asociatividad de `right-to-left`, es decir que las operaciones se realizan **primero de derecha a izquierda**. En este caso, primero se realiza `b = c` y luego `a = b` (en realidad al resultado de `b = c`, que retorna el valor que se está asignando). Por lo tanto al final de todo, todas las variables van a tener el valor `3`. Si la asociatividad hubiese al revés, todos las variables tendrían el valor `1`.

## Math

Los operadores matemáticos trabajan en python tal como lo harían en su calculadora.

#### + - * / =

```Python
1 + 1 = 2
2 * 2 = 4
2 - 2 = 0
2 / 2 = 1
```

#### %

Algo que quizás no haya visto antes es el Módulo (`%`), este operador matemático dividirá los dos números y devolverá el resto.

```Python
21 % 5 = 1
21 % 6 = 3
21 % 7 = 0
```

