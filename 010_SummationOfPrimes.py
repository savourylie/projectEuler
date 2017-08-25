def prime(num):
    """ (int) -> list of int

    Return a list of prime numbers that are less than num.

    >>> prime(10)
    [2, 3, 5, 7]

    >>> prime(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """

    test = True
    result = []
    j = 2

    for i in range(2, num):
        while (j < i and test == True):
            if i % j == 0:
                test = False
            j = j + 1

        j = 2
        
        if test == True:
            result.append(i)
            
        test = True

    return result
    
def sumPrime(num):
    """ (int) -> int

    Return the sum of primes below num.
    
    >>> sumPrime(10)
    17
    >>> sumPrime(25)
    100
    """

    result = 0
    
    x = prime(num)

    for i in x:
        result = result + i

    return result 
