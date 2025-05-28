
def is_it_prime(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("The number must be an integer.")      
     
    if num == 2:
        return True

    if num <= 1 or num % 2 == 0:
        return False
    
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True

def list_that_returns_primes(full_list: list[int]) -> list[int]:
    returned_list = []
    
    if not isinstance(full_list, list):
        raise TypeError("You must enter a list.")
    
    for element in full_list:
        if is_it_prime(element):
            returned_list.append(element)
    return returned_list

