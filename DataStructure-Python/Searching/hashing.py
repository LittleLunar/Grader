def isPrime(x):
    for i in range(2, x):
        if x % 2 == 0:
            return True
    return False

def findPrime(x):
    i = x
    while True:
        if isPrime(i):
            return i
        i += 1

