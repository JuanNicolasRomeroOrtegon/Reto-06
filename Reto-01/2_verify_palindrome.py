
def verify_palindrome(word: str) -> bool:

    if not isinstance(word, str):
        raise TypeError("The word must be a string.")

    if word == "":
        raise ValueError("Empty string is not a valid input.")

    word = word.lower()
    for x in range(len(word) // 2):
        if word[x] != word[-x-1]:
            return False
    return True




