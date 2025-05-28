
def basic_operations(num1: int, num2: int, election: str) -> float: 
    if not isinstance(election, str):
        raise TypeError("Your election must be a string.")
    
    if not isinstance(num1, (int, float)):
        raise TypeError("The number must be int or float.")
    
    if not isinstance(num2, (int, float)):
        raise TypeError("The number must be int or float.")

    match election: 
        case "+": 
            return num1 + num2 
        case "-": 
            return num1 - num2 
        case "*": 
            return num1 * num2
        case "/":   
            if num2 == 0: 
                raise ValueError("Division by zero isn't allowed")
            return num1 / num2
        case _: 
            raise ValueError("No valid operation selected")

