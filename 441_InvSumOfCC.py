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
    
def R(num):
    """ (int) -> number

    Return the sum of 1/(p*q) for all integer pairs p and q that satisfy

    1. 1 <= p < q <= num
    2. p + q >= M
    3. p and q are coprime.
    
    >>> R(2)
    0.5
    >>> R(3)
    1
    """

    M = num
    R_sum = 0
    
    for q in range(1, M + 1):
        for p in range(1, q):
            if p + q >= M and gcd(p, q) == 1:
                R_sum = R_sum + 1/(p*q)                
                    
    return R_sum


def S(num):
    """ (int) -> number

    Return the sum of R(i) for 2 <= i <= num.
    >>> S(2)
    0.5
    >>> S(10)
    6.9147
    >>> S(100)
    58.2962
    """

    S_sum = 0
    
    for i in range(2, num + 1):
        S_sum = S_sum + R(num)
        
    return S_sum
