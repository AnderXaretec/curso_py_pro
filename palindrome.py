def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::1]
    