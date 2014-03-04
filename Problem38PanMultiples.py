def pandigital(num):
    """ (int) -> bool

    Return True if num is pandigital, and False otherwise.
    
    >>> pandigital(192384576)
    True
    >>> pandigital(987654321)
    True
    >>> pandigital(839221287)
    False
    """

    s_num = str(num)
    checker = True
    i = 1

    if len(s_num) == 9:
        while i in range(1, len(s_num)+1):
            if str(i) not in s_num:
                checker = False
            i = i + 1
        
    else:
        checker = False

    return checker

def concat(num):
    """ (int) -> list of int

    Return the largest pandigital that can be achieved by concatenating the
    successive multiples of num.
    
    >>> concat(9)
    [918273645, 5]
    >>> concat(192)
    [192384576, 3]   
    """

    i = 1
    s_num = ''
    
    while len(s_num) < 9:
        s_num = s_num + str(num * i)
        i = i + 1

    n_s_num = int(s_num)
    
    if pandigital(n_s_num) == True:
        return [n_s_num, i - 1]

    else:
        return [0, 0]
    
def findNum():
    """
    """

    result = 0
    
    for i in range(50000):
        if concat(i)[0] > result:
            result = concat(i)[0]

    return result
        
        
