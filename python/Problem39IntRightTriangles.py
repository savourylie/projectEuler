import math

def hypo(num1, num2):
    """ (int, int) -> int

    Return the hypotenuse of a right triangle with sides of length num1, num2.
    
    >>> hypo(3, 4)
    5
    >>> hypo(5, 12)
    13
    """

    return math.sqrt(num1**2 + num2**2)

def IntRT(num):
    """ (int) -> list of list of int

    Return all the possible combination of sides that are integers and could
    form a right triangle, where the sum of the lengths of sides are no greater
    than num.
    
    >>> IntRT(120)
    [[20,48,52], [24,45,51], [30,40,50]]
    """

    result_list = []
    
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            k = math.sqrt(i**2 + j**2)
                
            if i + j + k == num and {i, j, k} not in result_list:
                result_list.append({i, j, k})
            
    return result_list

def findNum(num):
    """
    """

    count = 0
    target = 0
    
    for i in range(num + 1):
        if len(IntRT(i)) > count:
            count = len(IntRT(i))
            target = i

    return target
    
