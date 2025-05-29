# Reto-06
Uso de excepciones con su requerida identificación.

## En los códigos del Reto-01 se implementaron los siguientes cambios
### 1 - Basic Operations:

```python
if not isinstance(election, str):
    raise TypeError("Your election must be a string.")

if not isinstance(num1, (int, float)):
    raise TypeError("The number must be int or float.")

if not isinstance(num2, (int, float)):
    raise TypeError("The number must be int or float.")
```
Se verifica si los ***tipos*** de datos ingresados por el señor usuario son correctos.
```python
case "/":   
    if num2 == 0: 
        raise ValueError("Division by zero isn't allowed")
    return num1 / num2
case _: 
    raise ValueError("No valid operation selected")
```
No permitimos dividir por cero, validamos que el operador seleccionado por el usuario tenga sentido en el contexto.

### 2 - Verify Palindromes:

```python
if not isinstance(word, str):
    raise TypeError("The word must be a string.")

if word == "":
    raise ValueError("Empty string is not a valid input.")
```
En este caso también verificamos que los ***tipos*** de datos ingresados por el señor usuario sean correctos. Tampoco se puede ingresar una palabra vacía ya que no tiene sentido en este contexto.

### 3 - Return Prime Number:
```python
if not isinstance(full_list, list):
    raise TypeError("You must enter a list.")
```
Se verifica en la función principal si el dato ingresado es una lista.
```python
if not isinstance(num, int):
    raise TypeError("The number must be an integer.")   
```
Vemos si cada elemento de la lista es efectivamente un entero.

### 4 - Greater Sum of Consecutives:
```python
if len(num_list) == 0:
    raise ValueError("You cannot enter an empty list.")

if not isinstance(num_list, list):
    raise TypeError("You must enter a list.")

for element in num_list:
    if not isinstance(element, (int, float)):
        raise ValueError("The elements of your list must be integers or floats.")

if len(num_list) < 2:
    raise ValueError("The list must contain at least two integers.")
```
Verificamos que los tipos de datos tengan sentido, no permitimos ingresar listas vacías y la longitud de la lista ingresada no puede ser menor que dos, pues estamos verificando sumas consecutivas.

### 5 - Return Same Characters
```python
if not isinstance(original_list, list):
    raise TypeError("You must enter a list.")

if len(original_list) == 0:
    raise ValueError("You cannot enter an empty list.")

for element in original_list: 
    if not isinstance(element, str):
        raise TypeError("All the elements in your list must be strings.")
    if element == "":
        raise ValueError("The elements in the list cannot be an empty string.")
```
Se comprueban los tipos de datos y que ningun dato sea vacío.

## Cambios referentes al paquete ***Shape***

### Módulo line:
```python
if not isinstance(start_point, Point) or not isinstance(end_point, Point):
    raise TypeError("The data entered must be Points.")

if start_point == end_point:
    raise ValueError("The points must be differents") 
```
Se verifica que la entrada de los datos sea correcta, no permite que dos puntos sean los mismos ya que no se forma una línea.
```python
if not isinstance(start_point, Point):
    raise TypeError("You must enter a Point")
if start_point == self._end_point:
    raise ValueError("The points must be differents")

if not isinstance(end_point, Point):
    raise TypeError("You must enter a Point")
if end_point == self._start_point:
    raise ValueError("The points must be differents")
```
Hace las mismas verificaciones pero ahora en los setters.

### Módulo point:
```python
if not isinstance(x, int) or not isinstance(y, int):
    raise TypeError("You must enter integers.")

if not isinstance(x, int):
    raise TypeError("You must enter integers.")

if not isinstance(y, int):
    raise TypeError("You must enter integers.")

if not isinstance(other_point, Point):
    raise TypeError("You must enter a Point.")
```
Verifica las entradas de los datos en los diferentes métodos de la clase.

### Módulo shape:
```python
if (not isinstance(is_regular, bool) or not isinstance(vertices, list) 
        or not isinstance(edges, list)) or not isinstance(inner_angles, list):
    raise TypeError("You must validate the type of data entered.")

for element in vertices:
    if not isinstance(element, Point):
        raise TypeError("The elements in vertices must be Points.")

for element in edges:
    if not isinstance(element, Line):
        raise TypeError("The elements in edges must be Lines.")

for element in inner_angles:
    if not isinstance(element, float):
        raise TypeError("The elements in inner_angles must be floats")

if not vertices or not edges or not inner_angles:
    raise ValueError("The lists of data cannot be empty")
```
Verifica la entrada de los datos como ya se venía haciendo.

```python
if len(vertices) != len(inner_angles):
    raise ValueError("Number of vertices must match number of inner angles.") 
    #Any shape must have the same vertices and angles

if len(vertices) < 3:
    raise ValueError("A shape must have at least 3 vertices.")
if len(edges) < 3:
    raise ValueError("A shape must have at least 3 edges.")

if len(self._edges) == 0: 
    raise ValueError("The Shape doesn't have edges")

if len(self._inner_angles) == 0:
    raise ValueError("The Shape doesn't have angles")   
```
Comprueba propiedades básicas sobre cualquier polígono.

```python
if not isinstance(is_regular, bool):
    raise TypeError("is_regular must be a boolean.")

if not isinstance(vertices, list):
    raise TypeError("vertices must be a list.")
if not vertices:
    raise ValueError("vertices list cannot be empty.")
for vertex in vertices:
    if not isinstance(vertex, Point):
        raise TypeError("Each element in vertices must be a Point.")

if not isinstance(edges, list):
    raise TypeError("edges must be a list.")
if not edges:
    raise ValueError("edges list cannot be empty.")
for edge in edges:
    if not isinstance(edge, Line):
        raise TypeError("Each element in edges must be a Line.")
```
Comprobaciones equivalentes a las iniciales pero ahora en los respectivos setters.

### Módulo rectangle:
***Nota***: no se verifican los tipos de datos de vertices o edges puesto que rectangle hereda de shape.
```python
if len(edges) != 4:
    raise ValueError("A rectangle must have 4 edges")

if len(vertices) != 4:
    raise ValueError("A rectangle must have 4 vertices")
```
Se verifica que el rectángulo tenga 4 vértices y 4 bordes.

```python
if not isinstance(width, (int, float)):
    raise TypeError("You must enter a float or a integer.")
if width <= 0:
    raise ValueError("The width must be positive")

if not isinstance(height, (int, float)):
    raise TypeError("You must enter a float or a integer.")
if height <= 0:
    raise ValueError("The height must be positive")
```
Modificamos los setters para width y height.

### Módulo cuadrado:
***Nota***: como cuadrado hereda de rectángulo entonces no es necesario volver a verificar si el cuadrado tiene 4 bordes y 4 vértices.
```python
for element in edges:
    if side  != element.get_length():
        raise ValueError("The sides of a square must be equal.")
```
Se verifica que todos los lados del cuadrado sean iguales.
```python
if not isinstance(side, (int, float)):
    raise TypeError("Side must be a number.")
if side <= 0:
    raise ValueError("The side must be positive")
```
Comprobamos que los datos del setters estén correctos.

### Módulo triángulo: 

```python
if len(inner_angles) != 3:
    raise ValueError("A triangle must have 3 angles")

if len(vertices) != 3: 
    raise ValueError("A triangle must have 3 vertices")

if len(edges) != 3:
    raise ValueError("A triangle must have 3 edges")
        
if inner_angles[0] + inner_angles[1] + inner_angles[2] != 180:
    raise ValueError("The sum of the inner angles is not 180°")
```
Vemos si se tienen las características básicas que definen un triángulo: como que la suma de sus ángulos internos sea 180°.

Propiedad interesante:
```python
if (self._side1 + self._side2 <= self._side3 or
        self._side1 + self._side3 <= self._side2 or
        self._side2 + self._side3 <= self._side1):
            raise ValueError("The triangle inequality is not satisfied.")
```
Visualizamos si se cumple la desigualdad triangular, para saber si el triángulo está bien definido.

```python
if not isinstance(_side1, (int, float)):
    raise TypeError("You must enter a float or a integer.")

if _side1 <= 0:
    raise ValueError("El tamaño del lado debe ser positivo")
```
Para todos los lados y ángulos hacemos la verificación respectiva en los setters.

### Módulo equilateral:
```python
if (edges[0].get_length() != edges[1].get_length() or edges[0].get_length() 
!= edges[2].get_length()):
    raise ValueError("An equilateral triangle must have its sides " \
    "with the same length")
```
Analizamos si todos los lados son iguales para saber si está bien definido el triángulo equilátero.

### Módulo isósceles:
```python
sides = [self.get_side1(), self.get_side2(), self.get_side3()]
unique_sides = set(sides)
if len(unique_sides) != 2:
    raise ValueError("An isosceles triangle must have two equal sides exactly.")
```
Verificamos que solamente dos de los lados sean iguales para saber si, si se está definiendo un triángulo isóceles.

### Módulo scalene:
```python
if(edges[0].get_length() == edges[1].get_length() or edges[0].get_length() 
== edges[2].get_length() or edges[1].get_length() == edges[2].get_length()): 
    raise ValueError("All the sides must be different")
```
Miramos si los tres lados son diferentes entre sí para saber si la entrada de datos es correcta.

### Módulo trirectangle:
```python
if inner_angles[0] != 90 and inner_angles[1] != 90 and inner_angles[2] != 90:
    raise ValueError("At least one angle must be 90°")
```
Contemplamos que uno de los ángulos sea 90 grados para determinar que verdaderamente se está definiendo un triángulo rectángulo.
