import re

def is_palindrome(word):
    no_whitespace = re.sub(r"\s+", "", word)
    clean = re.sub(r"[^a-zA-Z0-9]", "", no_whitespace)

    if clean.lower() == clean[::-1].lower():
        return print("This is a Palindrome.")
    else:
        return print("This is not a Palindrome.")

is_palindrome("A man a plan a canal, Panama")