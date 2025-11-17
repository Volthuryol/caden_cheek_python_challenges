
def is_prime(num):

    if num < 2:
        return print(False)
    
    for i in range(2, num):
        if num % i == 0:
            return print(False)
        
    return print(True)

is_prime(11)