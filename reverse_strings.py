import re

def reverse_string(word):

    no_whitespace = re.sub(r"\s+", "", word)
    clean = re.sub(r"[^a-zA-Z0-9]", "", no_whitespace)

    # return print(word[::-1]) splicing

    reversed = ""
    for letter in clean:
        reversed = letter + reversed

    return print(reversed)

reverse_string("hello world")