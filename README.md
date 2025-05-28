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
Verificamos que los tipos de datos tengan sentido, no permitimos ingresar listas vacías y la longitud de la lista ingresada no puede ser menor que dos pues estamos verificando sumas consecutivas.

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
