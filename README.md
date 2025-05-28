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

    if not isinstance(num_list, list)   :
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
        #The points must be differente because if they're equal we do not get a line
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
Comprobaciones equivalentes a las iniciales pero ahora en los respectivos setters
