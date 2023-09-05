#Calculate the sum of the proper divisors of a number.

def d(num):
    """ (int) -> int

    Return the sum of the proper divisor of num.
    
    >>> d(220)
    284
    >>> d(284)
    220
    >>> d(10)
    8    
    """

    divisor = []
    
    for i in range(1, num):
        if num % i == 0:
            divisor.append(i)

    return sum(divisor)

#Check if a number is abundant.

def abundant(num):
    """ (int) -> bool

    Return True if num is an abundant number and False otherwise.
    
    >>> abundant(9)
    False
    >>> abundant(12)
    True
    """

    checker = False

    if d(num) > num:
        checker = True

    return checker

#Find all the abundant numbers under a given number.

def abundantNum(num):
    """ (int) -> list of int

    Return a list of abundant numbers under num.
    
    """

    result_list = []
    
    for i in range(num):
        if abundant(i):
            result_list.append(i)

    return result_list
        
def notAbundantSum(num):
    """ int -> int

    Return a list of numbers that are not sums of two abundant numbers.

    """

    aNum_list = abundantNum(num)
    result_list = []
    
    for i in range(len(aNum_list)):
        for j in range(len(aNum_list)):
            if aNum_list[i]+aNum_list[j] not in result_list and aNum_list[i]+aNum_list[j] <= num:
                result_list.append(aNum_list[i]+aNum_list[j])

    notSum = 0
    notResult_list = []
    
    for k in range(1, max(result_list)):
        if k not in result_list and k not in notResult_list:
            notSum = notSum + k
            notResult_list.append(k)

    return [notResult_list, notSum]
