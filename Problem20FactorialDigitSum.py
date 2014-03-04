import math

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
