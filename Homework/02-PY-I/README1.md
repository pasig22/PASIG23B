# Python
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

#### En esta lección cubriremos:

* Identación
* Funciones
* Control de flujo y operadores de comparación

## Identación
Para hablar de estructuras de control de flujo en Python, es imprescindible primero, hablar de identación.

**¿Qué es la identación?** En un lenguaje informático, la identación es lo que la sangría al lenguaje humano escrito (a nivel formal). Así como para el lenguaje formal, cuando uno redacta una carta, debe respetar ciertas sangrías, los lenguajes informáticos, requieren una identación.

No todos los lenguajes de programación, necesitan de una identación, aunque sí, se estila implementarla, a fin de otorgar mayor legibilidad al código fuente. Pero en el caso de Python, la identación es obligatoria, ya que de ella, dependerá su estructura.

Una identación de 4 (cuatro) espacios en blanco, indicará que las instrucciones identadas, forman parte de una misma estructura de control.

P.E
Una estructura de control, entonces, se define de la siguiente forma:
```Python
estructura_de_control:
	expresiones # la identación es el espacio que se deja al inicio.
```


## Funciones

Las funciones son una parte muy importante de todo lenguaje de programacion y sobre todo en Python. Són tipos particulares de objetos, llamados ***callable objects*** u objetos invocables, por lo que tienen las mismas propiedades que cualquier objeto.

Ahora que tenemos un conjunto de variables, necesitamos funciones para calcularlas, cambiarlas, hacer algo con ellas. Formas en que podemos construir una función.

```Python
def miFuncion():
	#Tú código
```

Usaremos la primera forma en esta lección y hablaremos sobre las otras formas en próximas lecciones.

### Anatomía de una Función

```Python
def miFuncion():
	#Tú código
```

Una función comenzará con la palabra clave `def`, esto le dice a lo que sea que esté ejecutando tu programa que lo que sigue es una función y que debe tratarse como tal. Después de eso viene el nombre de la función, nos gusta dar nombres de funciones que describan lo que hacen. Luego viene un paréntesis abierto y uno cercano. Y finalmente, abra y cierre los corchetes. Entre estos corchetes es donde irá todo nuestro código a ejecutar.

```Python
def logHola():
    print('hola!')

logHola()
# Resultado: hola
```

En este ejemplo declaramos una función `logHola` y la configuramos en `print('hola')`. Entonces podemos ver que para ejecutar esta función, necesitamos escribir el nombre y los paréntesis. Esta es la sintaxis para ejecutar una función. Una función siempre necesita paréntesis para ejecutarse.

### Argumentos

Ahora que podemos ejecutar una función básica, vamos a comenzar a pasarle argumentos.

```Python
def logHola(nombre):
    print('Hola, ' + nombre)

logHola('Martin') # se invoca a la función logHola y se le envia un argumento
```

Si agregamos una variable a los paréntesis cuando declaramos la función, podemos usar esta variable dentro de nuestra función. Iniciamos el valor de esta variable pasándola a la función cuando la llamamos. Entonces en este caso `nombre = 'Martin'`. También podemos pasar otras variables a esto:

```Python
def logHola(nombre):
    print( 'Hola', nombre)

miNombre = 'Antonio'
logHola(miNombre) # se invoca a la función logHola y se le envia un argumento
```

Podemos agregar múltiples argumentos colocando una coma entre ellos:

```Python
def sumarDosNumeros(a, b):
  suma = a + b
  return suma


sumarDosNumeros(1, 5); # se invoca a la función logHola y se le envia un argumentos
```

### Declaración "return"

En el ejemplo anterior presentamos la declaración `return`. No vamos a usar `print` con todo lo que salga de una función. Lo más probable es que queramos devolver algo. En este caso es la suma de los dos números. Piense en la declaración de retorno ("return") como la única forma en que los datos escapan de una función. No se puede acceder a nada más que a lo que se devuelve fuera de la función. También tenga en cuenta que cuando una función golpea una declaración de retorno, la función detiene inmediatamente lo que está haciendo y "devuelve" lo especificado.

```Python
def dividirDosNumeros(a, b):
  producto = a / b
  return producto


dividirDosNumeros(6, 3) # 2
print(producto) // undefined
```

Si intentamos `print` algo que declaramos dentro de la función, devolverá `undefined` porque no tenemos acceso a él fuera de la función. Esto se llama Scope ("alcance"). La única forma de acceder a algo dentro de la función es devolverlo.

También podemos establecer variables para igualar lo que devuelve una función.

```Python
def restarDosNumeros(a, b):
  diferencia = a - b
  return diferencia

diferenciaDeResta = restarDosNumeros(10, 9);
print(diferenciaDeResta) # 1
print(diferencia)	# undefined
```

**Podemos ver que la diferencia se establece dentro de la función. La variable dentro de la función solo pertenece dentro de la función.**

## Control de flujo y operadores de comparación

En este ejemplo, vamos a utilizar operadores de control de flujo y comparación. El flujo de control ("control flow") es una forma de que nuestra función verifique si algo es `true`, y ya sea ejecutando el código suministrado si es así o avanzando si no lo es. Para esto usaremos la palabra clave `if`:

```Python
def puedeManejar(edad):
    if edad > 18:
        return true
    else:
    return false

puedeManejar(22) # true
```

Aquí estamos tomando un número (`edad`) y verificando si la declaración es `true` (`22>18`), lo es, por lo que devolveremos `true`, y la función se detendrá. Si no es así, omitirá ese código y la función devolverá `false`.

El símbolo "mayor que" (`>`) que ve en el último ejemplo se llama *Operador de comparación*. Los operadores de comparación evalúan dos elementos y devuelven ***verdadero*** o ***falso***. Estos operadores son: `<`, `<=`, `>`, `> =`, `===`, `! ==`. Aprenderemos más sobre estos operadores en la próxima lección.

## Recursos adicionales

* [El Libro De Python](https://ellibrodepython.com/)
* [Python: Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)
* [Python: El tutorial de Python](https://docs.python.org/es/3/tutorial/index.html)

## Homework

Completa la tarea descrita en el archivo [README] que se ubica en la carpeta de Homework

<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Haz con cluido esta sección, bien hecho.
      </a>
    </td>
  </tr>
</table>

---

#### Si tienes dudas sobre este tema, NO dudes en escribir.
