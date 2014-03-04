import math

def factorialDigitSum(num):
    """ (int) -> int

    Return the sum of all the digit fifth power of num.
    
    >>> factorialDigitSum(145)
    145
    >>> factorialDigitSum(45023)
    153
    """
    s_num = str(num)
    digit = 0
    factorialDigitSum = 0

    for i in range(len(s_num)):
                   digit = (num // 10**i) % 10
                   factorialDigitSum = factorialDigitSum + math.factorial(digit)

    return factorialDigitSum

def findTheNumbers():
    """
    """
    
    i = 0
    result_list = []
    
    while i <= 10000000:

        i = i + 1
        
        if i == factorialDigitSum(i):
            result_list.append(i)

        if i == 100:
            print(i)

        if i == 500:
            print(i)
            
        if i == 1000:
            print(i)

        if i == 5000:
            print(i)

        if i == 10000:
            print(i)

        if i == 50000:
            print(i)

        if i == 100000:
            print(i)

        if i == 500000:
            print(i)

        if i == 1000000:
            print(i)

        if i == 5000000:
            print(i)

        if i == 10000000:
            print(i)
            
    return result_list
