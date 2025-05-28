
def find_max_consecutive_sum(num_list: list) -> int:

    if len(num_list) == 0:
        raise ValueError("You cannot enter an empty list.")

    if not isinstance(num_list, list)   :
        raise TypeError("You must enter a list.")
    
    for element in num_list:
        if not isinstance(element, (int, float)):
            raise ValueError("The elements of your list must be integers or floats.")
    
    if len(num_list) < 2:
        raise ValueError("The list must contain at least two integers.")
    
    greater = num_list[0] + num_list[1]
    for x in range(len(num_list) - 1):
        if num_list[x] + num_list[x+1] > greater:
            greater = num_list[x] + num_list[x+1]
    return greater

