
def sort_characters(original_list: list[str]) -> list[list[str]]:
    return [sorted(word) for word in original_list]

def words_with_the_same_characters(sorted_letters: list[list[str]]) -> list[str]:
    same_characters: list[list[str]]

    same_characters = []
    for x in range(len(sorted_letters) - 1):
        #We compare each word
        for y in range(x + 1, len(sorted_letters)):
            # We do this to avoid repetitions:
            if sorted_letters[x] == sorted_letters[y] and (
            sorted_letters[x] not in same_characters):
                same_characters.append(sorted_letters[x])
                
    return same_characters

def return_words(original_list: list[str]) -> list[str]:
    same_words: list

    if not isinstance(original_list, list):
        raise TypeError("You must enter a list.")

    if len(original_list) == 0:
        raise ValueError("You cannot enter an empty list.")

    for element in original_list: 
        if not isinstance(element, str):
            raise TypeError("All the elements in your list must be strings.")
        if element == "":
            raise ValueError("The elements in the list cannot be an empty string.")

    sorted_letters = sort_characters(original_list)
    same_characters = words_with_the_same_characters(sorted_letters)

    same_words = []
    for x in range(len(same_characters)):
        for w in range(len(sorted_letters)):
            if same_characters[x] == sorted_letters[w]:
                same_words.append(original_list[w])
        
    return same_words


