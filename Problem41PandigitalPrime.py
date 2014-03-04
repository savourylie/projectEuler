import KuMath

def pandigital(num):
    """ int -> bool

    Return True is num is pandigital and False otherwise.
    
    >>> pandigital(2143)
    True
    >>> pandigital(2941)
    False
    >>> pandigital(12235)
    False
    >>> pandigital(54231)
    True
    """

    s_num = str(num)
    s_n_num = ''
    checker = True

    for i in range(len(s_num)):
        if s_num[i] not in s_n_num:
            s_n_num = s_n_num + s_num[i]
        else:
            checker = False

    if checker == True:
        for j in range(1, len(s_n_num)+1):
            if str(j) not in s_n_num:
                checker = False

    return checker
        
def findNumber(num):
    """
    """

    ans = 0

    for i in range(1, num+1):
        if pandigital(i) == True and i > ans and KuMath.isPrime(i) == True:
            ans = i

    return ans
            
