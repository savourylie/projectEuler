def primeTest(num):
    """ int -> bool

    Return True if num is prime and False otherwise.

    >>> primeTest(1)
    False
    >>> primeTest(2)
    True
    >>> primeTest(17)
    True
    >>> primeTest(20298)
    False    
    """

    test = True
    j = 2
    
    while (j < num and test == True):
        if num % j == 0:
            test = False
        j = j + 1

    if num == 1:
        test = True

    if num == 2:
        test = True

    if num < 0:
        test = False
        
    if test == True:
        return True

    else:
        return False

def numConsPrimes(tup_num):
    """ (tuple of int) -> int

    >>> numConsPrimes((1, 41))
    40
    >>> numConsPrimes((-79, 1601))
    80    
    """

    n = 0
    counter = 0
    checker = True
    
    while checker == True:
        if primeTest(n**2 + tup_num[0]*n + tup_num[1]):
            n = n + 1
            counter = counter + 1
        else:
            checker = False

    return counter

def mostConsPrimes(num):
    """ (int) -> list
    """

    max_count = 0
    result_list = []
    ab_result = []
    
    for a in range(-(num-1), num):
        for b in range(-(num-1), num):
            ab_result.append([(a, b), numConsPrimes((a, b))])

    for i in range(len(ab_result)):
        if max_count < ab_result[i][1]:
            max_count = ab_result[i][1]
            result_list = [ab_result[i][0], ab_result[i][0][0]*ab_result[i][0][1]]
        
    return result_list
