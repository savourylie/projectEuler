def pythTrip(num):
    """ (int) -> int

    Return an int that is the product of 3 elements of which the square sum
    of the two elements is equal to the square of the other, and the sum
    all the elements is equal to num

    >>> pythTrip(12)
    60
    >>> pythTrip(30)
    [5, 12, 13]
    780
    """

    test = False
    i = 0
    
    while (i < num and test == False):
        for j in range(i+1, num):
            for k in range(j+1, num):
                if i**2 + j**2 == k**2:
                    if i + j + k == num:
                        result = i*j*k
                        test = True
        i = i + 1
                        
    return result
