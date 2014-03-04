def distinctPowers(num):
    """ (int) -> int

    Return the number of distinct a**b for all 2 <= a, b, <= 5.
    
    >>> distinctPowers(5)
    15
    """

    result = 0
    result_list = []
    
    for i in range(2, num+1):
        for j in range(2, num+1):
            result = i**j
            if result not in result_list:
                result_list.append(result)

    return len(result_list)
