import random
import math
import itertools

#Calculate the sum of the digits of a number.

def digitSum(num):
    """ (int) -> int

    Return the sum of all the digits of num.
    
    >>> digitSum(35920)
    19
    >>> digitSum(4500988)
    34
    """
    s_num = str(num)
    digit = 0
    digitSum = 0

    for i in range(len(s_num)):
                   digit = (num // 10**i) % 10
                   digitSum = digitSum + digit

    return digitSum
                   
#Greatest common divisor function.

def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b, r)
    if a < b:
        r = b % a
        if r == 0:
            return a
        else:
            return gcd(a, r)
    if a == b:
        return a

#Give a list of all the permutations of a string of int.
def permute(num_str):
    """ (str of int) -> list of str

    Return all of the permutations of the digits from num_list in
    lexicographic order.
    
    >>> permute('012')
    ['012', '021', '102', '120', '201', '210']
    >>> permute('01')
    ['01', '10']
    """

    perms = [''.join(p) for p in itertools.permutations(num_str)]

    return perms

#Prime checker.
def isPrime(num):
    """ (int) -> bool

    Return True if num is a prime and False otherwise.

    >>> isPrime(10)
    False
    >>> isPrime(228)
    False
    >>> isPrime(37)
    True
    """

    test = True
    result = []
    j = 2

    while (j < num and test == True):
        if num % j == 0:
            test = False
        else:
            j = j + 1

    if num <= 1:
        test = False
        
    return test
