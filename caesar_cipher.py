def caesar_cipher(text: str, shift: int):
    encrypt = []

    for letter in text:
        if letter.isalpha():
            start_alpha = ord('a') if letter.islower() else ord('A')
            crypt = (ord(letter) - start_alpha + shift) % 26 + start_alpha
            encrypt.append(chr(crypt))        
        else:
            encrypt.append(letter)
    
    return print("".join(encrypt))

caesar_cipher("Hello, World!", 3)

   


# test = "Hello world"
# test1 = []
# for i in test:
#     crypt = ord(i) + 2
#     #crypting = crypt + 2
#     print(crypt)
#     test1.append(crypt)

# print(test1)
# for i in test1:
#     decrypt = chr(i)
#     print(decrypt)

#print(ord("a"))