# Reto-06
Uso de excepciones con su requerida identificación.

### En los códigos del Reto-01 se implementaron los siguientes cambios
## Basic Operations:

```python
if not isinstance(election, str):
        raise TypeError("Your election must be a string.")
    
    if not isinstance(num1, (int, float)):
        raise TypeError("The number must be int or float.")
    
    if not isinstance(num2, (int, float)):
        raise TypeError("The number must be int or float.")
```
