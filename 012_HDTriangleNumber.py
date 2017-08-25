def triNumber(number):
    """ (int) -> int

    Return the numberth of triangular number.

    >>> triNumber(5)
    15
    >>> triNumber(7)
    28
    """

    sum = 0
    
    for i in range(number + 1):
        sum = sum + i

    return sum

def divisorFinder(number):
    """ (int) -> [list, int]

    Return a list of the positive divisors of number.
    
    >>> divisorFinder(10)
    [[1, 2, 5, 10], 4]
    >>> divisorFinder(28)
    [[1, 2, 4, 7, 14, 28], 6]
    """

    result = 0
    result_list = []
    counter = 0
    
    for i in range(1, number + 1):
        if number % i == 0:
            result = i
            result_list.append(result)
            counter = counter + 1

    return [result_list, counter]

def leastFinder(num):
    """ (int) -> int

    Return the first number to have num divisors.
    
    >>> leastFinder(6)
    12
    """

    checker = False
    i = 0

    while checker == False:
        i = i + 1
        if divisorFinder(i)[1] >= num:
            return i

def solution(num):
    checker = False
    i = 0

    while checker == False:
        i = i + 1

        if divisorFinder(triNumber(i))[1] >=num:
            return triNumber(i)
        
    
##    
##    while checker == False:
##        i = i + 1
##        if divisorFinder(triNumber(i))[1] > num:
##            checker = True
##        if i == 100:
##            print(i)
##        if i == 500:
##            print(i)            
##        if i == 1000:
##            print(i)
##        if i == 5000:
##            print(i)
##        if i == 10000:
##            print(i)
##        if i == 50000:
##            print(i)
##        if i == 100000:
##            print(i)
##        if i == 500000:
##            print(i)
##        if i == 1000000:
##            print(i)
##        if i == 5000000:
##            print(i)
##        if i == 10000000:
##            print(i)
##        if i == 50000000:
##            print(i)
##        if i == 100000000:
##            print(i)
##        if i == 500000000:
##            print(i)
##        if i == 1000000000:
##            print(i)
##        if i == 5000000000:
##            print(i)
##        if i == 10000000000:
##            print(i)

    return i
