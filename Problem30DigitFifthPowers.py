def powerSum(num1, num2):
    """ (int, int) -> int

    Return num1 * (10**0) + ... + num1 * (10**(num2 -1)).
    
    >>> powerSum(9, 5)
    99999
    >>> powerSum(3, 9)
    333333333
    """

    result = 0
    
    for i in range(num2):
        result = result + num1 * (10**i)

    return result

def fifthDigitSum(num):
    """ (int) -> int

    Return the sum of all the digit fifth power of num.
    
    >>> fifthDigitSum(35920)
    62449
    >>> fifthDigitSum(4500988)
    128734
    """
    s_num = str(num)
    digit = 0
    fifthDigitSum = 0

    for i in range(len(s_num)):
                   digit = (num // 10**i) % 10
                   fifthDigitSum = fifthDigitSum + digit**5

    return fifthDigitSum

def findTheNumbers():
    """
    """
    
    i = 0
    result_list = []
    
    while i <= 1000000:

        i = i + 1
        
        if i == fifthDigitSum(i):
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
            
    return result_list
