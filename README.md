# Curso-Practico-de-Python-Creacion-de-un-CRUD

Curso Practico de Python: Creacion de un CRUD

<h2>Content List</h2>

- [Guía de Instalación y Conceptos Básicos](#guía-de-instalación-y-conceptos-básicos)
- [Archivos y Slides del Curso Práctico de Python](#archivos-y-slides-del-curso-práctico-de-python)
- [Por qué Programar con Python ?](#por-qué-programar-con-python)
- [Operadores Matemáticos](#operadores-matemáticos)
- [Variables y Expresiones](#variables-y-expresiones)
- [Presentación del Proyecto](#presentación-del-proyecto)
- [Funciones](#funciones)
- [Usando Funciones en Nuestro Proyecto](#usando-funciones-en-nuestro-proyecto)
- [Operadores Lógicos](#operadores-lógicos)
- [ Esctructuras Condicionales](#esctructuras-condicionales)
- [Strings en Python](#strings-en-python)
- [Operaciones con Strings en Python](#operaciones-con-strings-en-python)
- [Operaciones con Strings y el Comando Update](#operaciones-con-strings-y-el-comando-update)
- [Operaciones con Strings y el Comando Delete](#operaciones-con-strings-y-el-comando-delete)
- [Operaciones con Strings: Slices en Python](#operaciones-con-strings-slices-en-python)
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Iterators and Generators](#iterators-and-generators)
- [Uso de Listas](#uso-de-listas)
- [Operaciones con Listas](#operaciones-con-listas)
- [Agregando Listas a Nuestro Proyecto](#agregando-listas-a-nuestro-proyecto)


## Guía de Instalación y Conceptos Básicos

Python es un lenguaje de programación creado por Guido Van Rossum, con una sintaxis muy limpia, ideado para enseñar a la gente a programar bien. Se trata de un lenguaje interpretado o de script.

<h3>Ventaja de python</h3>

* **Legible**: sintaxis intuitiva y estricta.
* **Productivo**: ahorra mucho código.
* **Portable**: para todo sistema operativo.
* **Recargado**: viene con muchas librerías por defecto.

<h3>Instalación de python</h3>

Existen dos versiones de Python que tienen gran uso actualmente, Python 2.x y Python 3.x, para este curso necesitas usar una versión 3.x

Para instalar Python solo debes seguir los pasos dependiendo del sistema operativo que tengas instalado.

<h4>Windows</h4>

Para instalar Python en Windows ve al sitio [Web de Python](https://www.python.org/downloads/) y presiona sobre el botón Download Python 3.x.x

Se descargará un archivo de instalación con el nombre python-3.x.x.exe , ejecútalo. Y sigue los pasos de instalación.

Al finalizar la instalación haz lo siguiente para corroborar una instalación correcta

1. Presiona las teclas Windows + R para abrir la ventana de Ejecutar.
2. Una vez abierta la ventana Ejecutar escribe el comando cmd y presiona ctrl+shift+enter para ejecutar una línea de comandos con permisos de administrador.
3. Windows te preguntará si quieres abrir el Procesador de comandos de Windows con permisos de administrador, presiona sí.
4. En la línea de comandos escribe python. 


<h4>MacOS</h4>

La forma sencilla es tener instalado [homebrew](https://brew.sh/) y usar el comando:

**Para instalar la Versión 2.7**
```bash
brew install python
```

Para instalar la Versión 3.x

```bash
brew install python3
```

<h4>Linux</h4>

Generalmente Linux ya lo trae instalado, para comprobarlo puedes ejecutar en la terminal el comando

Versión 2.7
```bash
python -v
```
Versión 3.x
```bash
python3 -v
```

Si el comando arroja un error quiere decir que no lo tienes instalado, en ese caso los pasos para instalarlo cambian un poco de acuerdo con la distribución de linux que estés usando. Generalmente el gestor de paquetes de la distribución de Linux tiene el paquete de Python

Si eres usuario de Ubuntu o Debian por ejemplo puedes usar este comando para instalar la versión 3.1:

```bash
$ sudo apt-get install python3.1
```

Si eres usuario de Red Hat o Centos por ejemplo puedes usar este comando para instalar python
```bash
$ sudo yum install python
```

<h3>Antes de empezar:</h3>

Para usar Python debemos tener un editor de texto abierto y una terminal o cmd (línea de comandos en Windows) como administrador.

Para ejecutar Python abre la terminal y escribe:

```bash
python
```

Te abrirá una consola de Python, lo notarás porque el prompt cambia y ahora te muestra tres simbolos de mayor que ```>>>``` y el puntero adelante indicando que puedes empezar a ingresar comandos de python.

```
 >>> 
 ```

En éste modo puedes usar todos los comandos de Python o escribir código directamente.

*Si deseas ejecutar código de un archivo sólo debes guardarlo con extension.py y luego ejecutar en la terminal:
```
 $ python archivo.py
 ```

Ten en cuenta que para ejecutar el archivo con extensión “.py” debes estar ubicado en el directorio donde tienes guardado el archivo.

Para salir de Python y regresar a la terminal debes usar el comando exit()

Cuando usamos Python debemos atender ciertas reglas de la comunidad para definir su estructura. Las encuentras en el libro [PEP8](https://peps.python.org/pep-0008/).

<h3>Tipos de datos en Python</h3>

* **Enteros (int)**: en este grupo están todos los números, enteros y long:

ejemplo: 1, 2.3, 2121, 2192, -123

* **Booleanos (bool)**: Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ):

ejemplo: True, False

* **Cadenas (str)**: Son una cadena de texto :

ejemplos: “Hola”, “¿Cómo estas?”

* **Listas**: Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:

ejemplos: [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ]

* **Diccionarios**: Son un grupo de datos que se acceden a partir de una clave:

ejemplo: {“clave”:”valor”}, {“nombre”:”Fernando”}

* **Tuplas**: también son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.

ejemplos: (1,2,3, ”hola” , (1,2,3) ), (1,“Hola”,True ) (Pero jamás podremos cambiar los elementos dentro de esa Tupla)

En Python trabajas con módulos y ficheros que usas para importar las librerías.

<h3>Funciones</h3>

Las funciones las defines con **def** junto a un nombre y unos paréntesis que reciben los parámetros a usar. Terminas con dos puntos.

**def nombre_de_la_función(parametros)**:

Después por indentación colocas los datos que se ejecutarán desde la función:
```python
 >>> def my_first_function():
 ...	return “Hello World!” 
 ...    
 >>> my_first_function()
Hello World!
```

<h3>Variables</h3>

Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto.
```
 A = 3 
 B = A
 ```

<h3>Listas</h3>

Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.

```python
 >>> L = [22, True, ”una lista”, [1, 2]] 
 >>> L[0] 
 22
 ```

<h3>Tuplas</h3>

Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.

```python
 >>> T = (22, True, "una tupla", (1, 2)) 
 >>> T[0] 
 22
```

<h3>Diccionarios</h3>

En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

```python
 >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"} 
 >>> D["Kill Bill"]
 "Tamarino"
```
<h3>Conversiones</h3>

De flotante a entero:

```
 >>> int(4.3)
 4
```

De entero a flotante:
```
 >>> float(4) 
 4.0
```
De entero a string:

```
 >>> str(4.3) 
 "4.3"
```

De tupla a lista:

```
 >>> list((4, 5, 2)) 
 [4, 5, 2]
```

<h3>Operadores Comunes</h3>

Longitud de una cadena, lista, tupla, etc.:
```
 >>> len("key") 
 3
```
<h3>Tipo de dato:</h3>
```
 >>> type(4) 
 < type int >
```

Aplicar una conversión a un conjunto como una lista:
```
 >>> map(str, [1, 2, 3, 4])
 ['1', '2', '3', '4']
```

Redondear un flotante con x número de decimales:

```
>>> round(6.3243, 1)
 6.3
```
Generar un rango en una lista (esto es mágico):
```
 >>> range(5) 
 [0, 1, 2, 3, 4]
```

Sumar un conjunto:
```
 >>> sum([1, 2, 4]) 
 7
```
Organizar un conjunto:
```
 >>> sorted([5, 2, 1]) 
 [1, 2, 5]
```

Conocer los comandos que le puedes aplicar a x tipo de datos:

```
 >>>Li = [5, 2, 1]
 >>>dir(Li)
 >>>['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

‘append’, ‘count’, ‘extend’, ‘index’, ‘insert’, ‘pop’, ‘remove’, ‘reverse’, ‘sort’ son posibles comandos que puedes aplicar a una lista.

Información sobre una función o librería:
```
 >>> help(sorted) 
 (Aparecerá la documentación de la función sorted)
```

<h3>Clases</h3>

Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto. Para definir la clase usas_ class_ y el nombre. En caso de tener parámetros los pones entre paréntesis.

Para crear un constructor haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

```python
 >>> class Estudiante(object): 
 ... 	def __init__(self,nombre_r,edad_r): 
 ... 		self.nombre = nombre_r 
 ... 		self.edad = edad_r 
 ...
 ... 	def hola(self): 
 ... 		return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad) 
 ... 
 >>> e = Estudiante(“Arturo”, 21) 
 >>> print (e.hola())
 Mi nombre es Arturo y tengo 21
```

Lo que hicimos en las dos últimas líneas fue:

1. En la variable e llamamos la clase Estudiante y le pasamos la cadena “Arturo” y el entero 21.

2. Imprimimos la función hola() dentro de la variable e (a la que anteriormente habíamos pasado la clase).

Y por eso se imprime la cadena “Mi nombre es Arturo y tengo 21”

<h3>Métodos especiales</h3>

<h4>cmp(self,otro)</h4>

Método llamado cuando utilizas los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

<h4>len(self)</h4>

Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

<h4>init(self,otro)</h4>

Es un constructor de nuestra clase, es decir, es un “método especial” que se llama automáticamente cuando creas un objeto.

<h4>Condicionales IF</h4>

Los condicionales tienen la siguiente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que los elementos se cumplan.
```python
 if ( a > b ):
 	elementos 
 elif ( a == b ): 
 	elementos 
 else:
 	elementos
```

<h4>Bucle FOR</h4>

El bucle de for lo puedes usar de la siguiente forma: recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

```python
 for i in ____:
 	elementos
```

Ejemplo:
```python
 for i in range(10):
 	print i
```

En este caso recorrerá una lista de diez elementos, es decir el _print i _de ejecutar diez veces. Ahora i va a tomar cada valor de la lista, entonces este for imprimirá los números del 0 al 9 (recordar que en un range vas hasta el número puesto -1).

<h4>Bucle WHILE</h4>

En este caso while tiene una condición que determina hasta cuándo se ejecutará. O sea que dejará de ejecutarse en el momento en que la condición deje de ser cierta. La estructura de un while es la siguiente:
```python
 while (condición):
 	elementos
```

Ejemplo:

```python
 >>> x = 0 
 >>> while x < 10: 
 ... 	print x 
 ... 	x += 1
```

En este ejemplo preguntará si es menor que diez. Dado que es menor imprimirá x y luego sumará una unidad a x. Luego x es 1 y como sigue siendo menor a diez se seguirá ejecutando, y así sucesivamente hasta que x llegue a ser mayor o igual a 10.

## Archivos y Slides del Curso Práctico de Python 

* [Slides](https://drive.google.com/file/d/1uAC0egE_U6571mV8gHtHq5ahIbo9vd1e/view)

* [Repositorio](https://github.com/mfriascos/curso_Python3) Completo del Curso en el cual encontrarás todo el proyecto dividido en secciones tal como fue 

## Qué es la Programación? 

Python es uno de los lenguajes más emocionantes de la actualidad y puedes lograr muchas cosas con él. Este curso te va a servir como una introducción al lenguaje. 

<h3>Qué es la Programación</h3>

Es una disciplina que combina parte de otras disciplinas como las Matemáticas, Ingeniería y la Ciencia. Sin embargo, la habilidad más importante es resolver problemas. Es lo que harás todos los días como programador o programadora.

La programación es una secuencia de instrucciones que le damos a la computadora para que haga lo que nosotros deseamos. Podemos construir una aplicación web, móvil, un programa que lleve cohetes a la luna o marte, resolver problemas de finanzas.

La estructura de un programa. Casi todos los programas tienen un input, output, operaciones matemáticas, ejecución condicional y repeticiones

<h3>Objetivos del curso:</h3>

* Aprender a pensar como un Científico de la Computación
* Aprender a utilizar Python
* Entender las ventajas y desventajas de Python
* Aprender a construir una aplicación de línea de comandos.

## Por qué Programar con Python ? 

Python es uno de los mejores lenguajes para principiantes porque tiene una sintaxis clara, una gran comunidad y esto hace que el lenguaje sa muy amigable para los que están iniciando. 

Python está diseñado para ser fácil de usar, a diferencia de otros lenguajes donde la prioridad es ser rápido y eficiente. Python no es de los lenguajes más rápidos, pero casi nunca importa. 

Es el tercer lenguaje, según Github, entre los más populares. En StackOverflow se comenta que es uno de los lenguajes que mayor popularidad está obteniendo. 

**"Python cuando podamos, C++ cuando necesitemos"**

## Operadores Matemáticos 

En **Programación** estos operadores son muy similares a nuestras clases básicas de matemáticas. 

* ```//```: Es división de entero, básicamente tiramos la parte decimal 
* ```%```: Es el residuo de la división, lo que te sobra. 
* ```**```: Exponente

Los operadores son contextuales, dependen del tipo de valor. Un valor es la representación de una entidad que puede ser manipulada por un programa. 

Podemos conocer el tipo de calor con type() y nos devolverá algo similar a ```<class 'init'>, <class 'float'>, <class 'str'>```. Dependiendo del tipo los operadores van a funcionar de manera diferente. 

## Variables y Expresiones

Una variable es simplemente el contenedor de un valor. Es una forma de decirle a la computadora de que nos guarde un valor para luego usarlo. 

Python es un lenguaje **dinámico**, este concepto de privado y público se genera por convenciones del lenguaje. En programación el signo ```=```significa asignación. 

Si una variable está en mayúscula, usualmente se refiere a una constate, no debería resignarse . Es una conveción. 

<h3>Reglas de Variables</h3>

* Pueden contener números y letras 
* No deben comenzar con número
* Múltiples palabras se unen con _
* No se puede utilizar palabras reservadas

Expresiones son instrucciones para el interprete para evaluar la expresión. Los enunciados tienen efectos dentro del programa, como ```print```que genera un **output**

**PEMDAS** = Paréntesis, Exponente, Multiplicación-División, Adición-Sustracción. 

## Presentación del Proyecto 

Un vistazo al proyectode línea de comandos llamado Platzi Ventas la cual nos va a servir para manejar clientes, ventas, inventarios y generar algunos reportes. 

Desde la línea de comandos podemos crear un archivo con ```touch [nombre-del-archivo]```.

Escribiremos el primer archivo ```main.py```. 

## Funciones 

En el contexto de la programación las funciones son simplemente una agrupación de enunciados (**statments**) que tienen un nombre, debe ser descriptivo, pueden tener parámetros y puede regresar un valor después que se generó el cómputo. 

Python es un lenguaje que se conoce como *batteries include* (baterías incluidas) que signidica que tienen una librería estándar con muchas funciones y librerías. 

Para declarar funciones que no son las globales, las *built-in functions*, necesitamos importar un módulo. Con el keyword ```def```declaramos una función. 

<p align="center"><img width=85% src="./pictures/built-in-functions.webp"></p>

Información acerca de las built-in, se encuentra [aquí](https://docs.python.org/3/library/functions.html)

<h3>Funciones Lambda</h3>

Muchas veces llamadas "funciones anónimas", las funciones lambda en Python, no son más que una forma de definir una función común y corriente, de una única instrucción de código, en una única línea.

Es decir, una función lambda es la forma de definir una función que tradicionalmente podría escribirse de forma común, en una sola línea de código. Pero esto, solo podrá hacerse con aquellas funciones cuyo algoritmo, no posea más de una instrucción.

La siguiente función:

```python 
def mifuncion(nombre):
	return "Hola %s!" % nombre
```

Con lambda, podría definirse en una sola línea de código, ya que posee una única instrucción.

Para ello, se utilizaría la siguiente instrucción:

```python
mifuncion = lambda nombre: "Hola %s! % nombre
```

## Usando Funciones en Nuestro Proyecto. 

Añadimos funciones al archivo [main.py](/Platzi_Ventas/main.py)

## Operadores Lógicos 

Para compreender el flujo de nuestro programa debemos entender un poco sobre estructuras y expresiones booleanas 

* ```==``` Se refiere a igualdad, o comparación
* ```!=``` No hay igualdad
* ```>``` Mayor que 
* ```<``` Menor que
* ```>=``` Mayor o igual 
* ```<=``` Menor o igual
* ```and``` Unicamente es verdadero cuando **ambos** valores son verdaderos
* ```or``` Es verdadero cuando uno de los dos valores es verdadero
* ```not``` Es lo contrario al valor. Falso es verdadero. Verdadero es falso

## Esctructuras Condicionales 

En Python es importante la **Indentación**, de esa manera identifica donde empieza y termina un bloque de código sin necesidad de llaves {} como en otros lenguajes. 

Continuación del archivo main en el commit "Estructuras condicionales". 

## Strings en Python 

Los strings o cadenas de texto tienen un comportamiento distinto a otros tipos como los booleanos, enteros, floats. Las cadenas son secuencias de caracteres, todas se pueden acceder a través de un índice. 

Podemos saber la longitud de un *string*, cuántos caracteres se encuentran en esa secuencia. Lo podemos saber con la ***built-in funtion*** global llamada ```len```. 

Algo importante a tener en cuanta cuando hablamos se *strings* es que estos son inmutables, esto significa que cada vez que modificamos uno estamos generando un nuevo objeto en memoria. 

El índice de la primera letra es 0, en la programación se empieza a contar desde 0

<h3>Funciones de Strings</h3>

**Method** | **Description**
|:------------- | :-------------|
capitalize() | Convierte el primer carácter en mayúsculas
casefold() | Convierte una cadena en minúsculas
center() | Devuelve una cadena centrada
count() | Devuelve el número de veces que un valor especificado se produce en una cadena
encode() | Devuelve una versión codificada de la cadena
endswith() | Devuelve true si los extremos de cadena con el valor especificado
expandtabs() | Establece el tamaño de la pestaña de la cadena
find() | Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
format() | Formatos especifican los valores de una serie
format_map() | Formatos especifican los valores de una serie
index() | Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
isalnum() |Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos
isalpha() |Devuelve True si todos los caracteres de la cadena están en el alfabeto
isdecimal() | Devuelve True si todos los caracteres de la cadena son decimales
isdigit() | Devuelve verdadero si todos los caracteres de la cadena son dígitos
isidentifier() | Devuelve True si la cadena es un identificador
islower() | Devuelve verdadero si todos los caracteres de la cadena son minúsculas
isnumeric() | Devuelve verdadero si todos los caracteres de la cadena son numéricos
isprintable() | Devuelve verdadero si todos los caracteres de la cadena son imprimibles
isspace() | Devuelve True si todos los caracteres de la cadena son espacios en blanco
istitle() | Devuelve True si la cadena sigue las reglas de un título
isupper() | Devuelve True si todos los caracteres de la cadena son mayúsculas
join() | Se une a los elementos de un iterable al final de la cadena
ljust() | Devuelve una versión justificada izquierda de la cadena
lower() | Convierte una cadena en minúsculas
lstrip() | Devuelve una versión de ajuste izquierdo de la cuerda
maketrans() | Devuelve una tabla de traducción para ser utilizado en traducciones
partition() | Devuelve una tupla donde la cadena se separó en tres partes
replace() | Devuelve una serie en un valor especificado es reemplazado con un valor especificado
rfind() | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
rindex() | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
rjust() | Devuelve una versión justificada derecha de la cadena
rpartition() | Devuelve una tupla donde la cadena se separó en tres partes
rsplit() | Divide la cadena en el separador especificado y devuelve una lista
rstrip() | Devuelve una versión ajuste correcto de la cadena
split() | Divide la cadena en el separador especificado y devuelve una lista
splitlines() | Divide la cadena en los saltos de línea y devuelve una lista
startswith() | Devuelve true si la cadena comienza con el valor especificado
strip() | Devuelve una versión recortada de la cadena
swapcase() | Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa
title() | Convierte el primer carácter de cada palabra en mayúsculas
translate() | Devuelve una cadena traducida
upper() | Convierte una cadena en mayúsculas
zfill() | Rellena la cadena con un número determinado de valores de 0 a principios

## Operaciones con Strings en Python 

Los strings tienen varios métodos que nosotros podemos utilizar.

* ```upper```: convierte todo el string a mayúsculas
* ```lower```: convierte todo el string a minúsculas
* ```find```: encuentra el indice en donde existe un patrón que nosotros definimos
* ```startswith```: significa que empieza con algún patrón.
* ```endswith```: significa que termina con algún patrón
* ```capitalize```: coloca la primera letra en mayúscula y el resto en minúscula. 

```in``` y ```not in``` nos permite saber con cualquier secuencia sin una subsecuencia o substrings se encuentra adentro de la secuencia mayor.

```dir```: Nos dice todos los métodos que podemos utilizar dentro de un objeto.

```help```: nos imprime en pantalla el docstrings o comentario de ayuda o instrucciones que posee la función. Casi todas las funciones en Python las tienen.

[**Dunder methods**](https://docs.python.org/3/reference/datamodel.html#special-method-names): También conocidos como **magic methods** (métodos mágicos) o **special methods** (métodos especiales)

## Operaciones con Strings y el Comando Update 

En esta clase seguiremos construyendo nuestro proyecto **PlatziVentas**, agregaremos el comando **update** para poder actualizar nuestros clientes y pondremos en práctica lo aprendido en clases anteriores sobre Strings.

## Operaciones con Strings y el Comando Delete

CRUD 

**[C]reate
[R]ead
[U]pdate
[D]elete**

Es un modelo muy utilizado por cientificos de computadores. Se usa mucho en aplicaciones web, para construir modelos usables. 

## Operaciones con Strings: Slices en Python

Python tiene una de las sintaxis más poderosas para manipular secuencias, esta sintaxis se llama **slice** (Rebanada en español)

Se define de la siguiente forma:

```python
secuencia[comienzo:final:pasos]
```

## For Loops

Las iteraciones es uno de los comceptos más importantes en la programación. En Python existen muchas maneras de iterar pero las dos principales son los **for loops** y **while loops**. 

Los **for loops** nos permiten iterar a través de una secuencia y los while loops nos permiten iteran hasta cuando una condición se vuelva falsa. 

<h3>for loops</h3>

* Tienen dos keywords ```break```y ```continue```que nos permiten salir anticipadamente de la iteración
* Se usan cuando se quiere ejecutar varias veces una o varias instrucciones. 
* for [variable] in [secuencia]: 
Es una convención usar la letra ```i```como variable en nuestro for, pero podemos colocar la que queramos. 

```range```: Nos da un objeto rango, es un iterador sobre el cual podemos generar secuencias. 

## While Loops

Al igual que las For Loops, las while loops nos sirve para iterar, pero las for loops nos sirve para iterar a lo largo de una secuencia mientras que las while loops nos sirve para iterar mientras una condición sea verdadera. 

Si no tenemos un mecanismo para convertir el mecanismo en falsedad, entonces nuestro while loop se irá al infinito (infinite loop).

## Iterators and Generators 

Aunque no lo sepas, probablemente ya utilices iterators en tu vida diaria como programador de Python. Un iterator es simplemente un objeto que cumple con los requisitos del Iteration Protocol (protocolo de iteración) y por lo tanto puede ser utilizado en ciclos. Por ejemplo,

```python
for i in range(10):
    print(i)
```

En este caso, la función range es un iterable que regresa un nuevo valor en cada ciclo. Para crear un objeto que sea un iterable, y por lo tanto, implemente el protocolo de iteración, debemos hacer tres cosas:

* Crear una clase que implemente los métodos **iter** y **next**
* **iter** debe regresar el objeto sobre el cual se iterará
* **next** debe regresar el siguiente valor y aventar la excepción StopIteration cuando ya no hayan elementos sobre los cual iterar.

Por su parte, los generators son simplemente una forma rápida de crear iterables sin la necesidad de declarar una clase que implemente el protocolo de iteración. Para crear un generator simplemente declaramos una función y utilizamos el keyword yield en vez de return para regresar el siguiente valor en una iteración. Por ejemplo,

```python
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
```

Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y debemos crear una nueva instancia. Por ejemplo,

```python
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
...
double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona
```

## Uso de Listas 

Python y todos los lenguajes nos ofrecen constructos mucho más poderosos, haciendo que el desarrollo de nuestro software sea

* Más sofisticado
* Más legible
* Más fácil de implementar

Estos constructos se llaman Estructuras de Datos que nos permiten agrupar de distintas maneras varios valores y elementos para poderlos manipular con mayor facilidad.

Las listas las vas a utilizar durante toda tu carrera dentro de la programación e ingeniería de Software.

Las listas son una secuencia de valores. A diferencia de los strings, las listas pueden tener cualquier tipo de valor. También, a diferencia de los strings, son mutables, podemos agregar y eliminar elementos.

En Python, las listas son referenciales. Una lista no guarda en memoria los objetos, sólo guarda la referencia hacia donde viven los objetos en memoria

Se inician con ```[]``` o con la *built-in function* ```list```.

<h4>Particularidades de las listas</h4>

```python
countries = ['México','Venezuela','Colombia','Argentina']
ages = [12,18,24,34,50]

weights = [12,18,24,34,50]

# Las últimas listas viven en diferentes lugares de memoria, 
# a pesar de que sean iguales 

receta = ['Ensalada',2,'Lechugas',5,'Jitomates']

```

## Operaciones con Listas 

Ahora que ya entiendes cómo funcionan las listas, podemos ver qué tipo de operaciones y métodos podemos utilizar para modificarlas, manipularlas y realizar diferentes tipos de cómputos con esta Estructura de Datos.

* El operador **+(suma)** concatena dos o más listas.
* El operador ***(multiplicación)** repite los elementos de la misma lista tantas veces los queramos multiplicar
Sólo podemos utilizar **+(suma) y *(multiplicación)**.

Las listas tienen varios métodos que podemos utilizar.

* ```append``` nos permite añadir elementos a listas. Cambia el tamaño de la lista.
* ```pop``` nos permite sacar el último elemento de la lista. También recibe un índice y esto nos permite elegir qué elemento queremos eliminar.
* ```sort``` modifica la propia lista y ordenarla de mayor a menor. Existe otro método llamado sorted, que también ordena la lista, pero genera una nueva instancia de la lista
* ```del``` nos permite eliminar elementos vía indices, funciona con slices
* ```remove``` nos permite es pasarle un valor para que Python compare internamente los valores y determina cuál de ellos hace match o son iguales para eliminarlos.

<h3>Resume</h3>

Suma (+) Concatena dos o más listas:
```
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
```
Multiplicación (*) Repite la misma lista:
```
a=[1,2]
a * 2 —> [1,2,1,2]
```
Añadir elemento al final de la lista:
```
a=[1]
a.append(2)=[1,2]
```
Eliminar elemento al final de la lista:
```
a=[1,2]
b=a.pop()
a=[1]
```
Eliminar elemento dado un indice:
```
a=[1,2]
b=a.pop(1)
a=[2]
```
Ordenar lista de menor a mayor, esto modifica la lista inicial
```
a=[3,8,1]
a.sort() —> [1,3,8]
```
Ordenar lista de menor a mayor, esto NO modifica la lista inicial
```
a=[3,8,1]
a.sorted() —> [1,3,8]
```
Eliminar elementos de lista Elimina el elemento de la lista dado su indice
```
a=[1,2,3]
del a[0] —> a[2,3]
```
Eliminar elementos de lista Elimina el elemento de la lista dado su valor
```
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
```
Range creacion de listas en un rango determinado
```
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
```
Tamaño lista len Devuelve el valor del tamaño de la lista:
```
a=[0,2,4,6,8]
len(a)=5
```

## Agregando Listas a Nuestro Proyecto

<h3>Notas**</h3>

```index()``` Es un método que busca la posición de un elemento en una lista y nos regresa su posición. Y si hay varios elementos iguales, nos regresa el primer elemento. 
