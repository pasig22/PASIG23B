PYTHON
==================
<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Hacé click acá para dejar tu feedback sobre esta clase.
      </a>
    </td>
  </tr>
</table>

# Conceptos

#### Variables, expresiones y declaraciones

<div class="iframeContainer">
<iframe width="560" height="315" src="https://www.youtube.com/embed/cPtifhPOIPE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>
</div>

# Expressions

Una *expresión* es cualquier pedazo de código **que pueda ser evaluado a un valor**. Justamente por esto, las vamos a usar en lugares donde Python *espera un valor*. Por ejemplo, cómo cuando pasamos una expresión como argumento de una función.


Podemos decir que todo el código que escribimos en Python o "hace algo" o "retorna algo" (o una combinación de los dos). En la terminología de lenguajes de programación esta diferencia está clasificada en la definición de **expresiones** (expresiones) y **declaraciones** (sentencias).

Podriamos definir conceptualmente a ambas como:

- Una **expresión** siempre se convierte (retorna) un valor.
- Un **declaración** realiza una acción.

Cuando escribimos código, todo el tiempo mezclamos expresiones y statements para conseguir el resultado final. Por lo tanto, al principio es un poco díficil ver la diferencia entre las dos, pero vamos a intentar ejemplificar lo anterior:

```python
import Math
// retorna algo
1 + 1
Math.pow(2, 3) + 4
'hola' + ' soy una expression'
```
`1 + 1` intuitivamente se convierte o resuelve a `2`! eso es una expresión. Es cualquier cosa que escribamos y esperamos que se convierta en otro valor.

Según la documentación de Python, las expresiones se pueden clasificar en las siguientes categorías:

1. **Expresiones constantes**: estas son las expresiones que solo tienen valores constantes.

```Python
x = 15 + 1.3
print(x)
```
2. **Expresiones aritméticas**: una expresión aritmética es una combinación de valores numéricos, operadores y, a veces, paréntesis. El resultado de este tipo de expresión también es un valor numérico. Los operadores usados en estas expresiones son operadores aritméticos como suma, resta, etc. Aquí hay algunos operadores aritméticos en Python:

 | Operadores | Sintaxis | Marcha |
 | ----------- | ----------- |
 | + | x + y | Suma |
 | - | x – y | Sustracción |
 | * | x * y | Multiplicación |
 | / | x / y | División |
 | // | x // y | Cociente |
 | % | x % y | Resto |
 | ** | x ** y | exponenciación |
3. **Expresiones relacionales**: : en este tipo de expresiones, las expresiones aritméticas se escriben en ambos lados del operador relacional (> , < , >= , <=). Esas expresiones aritméticas se evalúan primero y luego se comparan según el operador relacional y producen una salida booleana al final. Estas expresiones también se denominan expresiones booleanas.
```Python
# Expresiones relacionales
a = 21
b = 13
c = 40
d = 37
p = (a + b) >= (c - d)
print(p)
```
4. **Expresiones lógicas**: Estos son tipos de expresiones que resultan en Verdadero o Falso. Básicamente especifica una o más condiciones. Por ejemplo, (10 == 9) es una condición si 10 es igual a 9. Como sabemos, no es correcto, por lo que devolverá False. Al estudiar expresiones lógicas, también nos encontramos con algunos operadores lógicos que se pueden ver en expresiones lógicas con mayor frecuencia. Aquí hay algunos operadores lógicos en Python:
|Operador	|Sintaxis|	Marcha
| ----------- | ----------- |
|y|	P y Q|	Devuelve verdadero si tanto P como Q son verdaderos; de lo contrario, devuelve falso
|o	|P o Q	|Devuelve verdadero si al menos uno de P y Q es verdadero
|no	|no p	|Devuelve verdadero si la condición P es falsa
```Python
P = (10 == 9)
Q = (7 > 5)
# Logical Expressions
R = P and Q
S = P or Q
T = not P
print(R)
print(S)
print(T)
```


### Expresiones Aritméticas

Son las expresiones que resuelven a un valor **númerico**. Por ejemplo:

```Python
10
1 + 10
2 * 16
```

### Expresiones de Strings

Son expresiones que resuelven a una **string**. Por ejemplo:

```Python
'hola'
'hola' + ' como va?'
```

## Expresiones lógicas

Son expresiones que resuelven a un valor **booleano**. Por ejemplo:

```Python
10 > 9
11 == 2
false
```

## Expresiones primarias

Son expresiones que se escriben por si mismas, y no utilizan ningún operador. Incluyen a valores literales, uso de variables, y algunos keywords de JS. Por ejemplo:

```Python
'hola'
23
true
this  # hace referencia al keyword this
numero # hace referencia a la variable numero
```

## Expresiones de asignación

Cuando utilizamos el operador `=` hablamos de un *assigment expression*. Está expresión retorna el valor asignado. Por ejemplo:

```Python
a = 1 # si probamos esto en la consola, vemos que retorna el valor 1.
var c = (a = 2) # vamos a ver que dentro de la variable c, está el valor retornado por la expresion `a = 2`
```

> Este es un caso muy particular, nótese que esta expresion retornar una valor, **pero a su vez hace algo**!! Ese algo, es guardar el valor a la derecha del signo `=` en la variable a la izquierda del signo `=`.
  Otra cosa a notar, es que si usamos el keyword `var` la expresión retorna `undefined`, es decir, no es lo mismo una asignación que una declaración de variables.

## Expresiones con efectos secundarios (side effects)

Son expresiones que al ser evaluadas retornan algo, pero a su vez tienen *un efecto secundario* (incrementar un valor, etc...). Por ejemplo:

```Python
contador++ # retorna el valor de contador e incrementa uno.
++contador # incrementa el valor de contador y retorna el valor;

mult *= 2 # multiplica mult por dos, asigna ese valor a mult y retorna el valor;
```

# Declaraciones (Statements) (sentencias)

Los *Statements* son instrucciones que le damos al intérprete de JS para que **haga algo**, ese algo puede ser: crear una variable, ejecutar un bloque de código N veces, ejecutar un bloque de código o no según una condición de verdad, declarar una función, etc...

Podemos clasificar a los Statements en las siguientes categorías:

### Declaración

Este tipo de statements indican al intérprete que declare variables o funciones, se utiliza el keyword `function` y `var`. Por ejemplo:

```Python
municipio # declaro la variable muncipio
clave  # declaro la variable clave

def suma(a, b):   # declaro la función suma;
  # bloque de código

```

> Habiamos dicho que por regla general lo que podamos pasarle a una función (por ejemplo, `console.log`) por argumento era una expresión... y muchas veces pasamos una declaración de una función por argumento. Esto sucede porque en JS existen tambien las **function expressions**.

#### Función de expresión vs función declaración

Cuando declaramos una función el intérprete puede *interpretarla* como un statement o cómo una expresión, dependiendo del contexto. Por ejemplo:

```Python
# función de declaración
def resta(a, b):
 # bloque de código

# función de expresión
resta = resta(a, b):
  # bloque de código
```

Cómo vemos en el ejemplo de arriba, el intérprete *hace algo*: declara la función. Por lo tanto es un statement. En cambio, en el segundo ejemplo, estamos haciendo una asignación, y la asignación espera una *expresión* en la parte de la derecha, asi que le estamos pasando un function expression.

> Nótese que un function expression puede no regresar valores si no son solicitadas.

### Declaraciones condicionales (Statements)

Estas declaraciones sirven para controlar el flujo de ejecución de código según si se cumple o no una condición. Por ejemplo:

```Python
if condicion1: # condicion puede ser cualquier expression!!
  # ejecuta este bloque si condicion es true
elif condicion2:
  # ejecuta este bloque de código si condicion no es true y condicion2 es true
else
  #ejecuta este bloque de código si condicion y condicion2 no son true.
```

### for (bucles) y loops

Estos statements también controlan el flujo de ejecución del código, pero hacen que un bloque se ejecute N veces (ej: `for`), o que la ejecución salte a otro contexto (ej: `return`). Por ejemplo:

```Python
var = 9
for i in range(var):
  # ejecuta este bloque de código 9 veces;

# loops
while var <= 9: # condicion es una expresión!!
  # ejecuta este código mientras condicion sea true;

```
