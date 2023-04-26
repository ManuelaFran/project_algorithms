def is_palindrome_iterative(word):
    if len(word) < 1:
        return False
    if str(word) == str(word)[::-1]:
        return True
    return False
