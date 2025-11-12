def reverse_string(word):

    # return print(word[::-1]) splicing

    reversed = ""
    for letter in word:
        reversed = letter + reversed

    return print(reversed)

reverse_string("hello world")