def squareSeq(tup_num):
    """ (tuple of int) -> list of int

    Return the Square sequence determined by the first two terms.
    
    >>> squareSeq((1, 9, 5))
    [1, 9, 25, 49, 81]
    >>> squareSeq((1, 3, 4))
    [1, 3, 13, 31]
    >>> squareSeq((1, 5, 4))
    [1, 5, 17, 37]
    >>> squareSeq((1, 7, 4))
    [1, 7, 21, 43]
    """

    checker = True
    squareSeq = [tup_num[0], tup_num[1]]
    i = 0
    
    while checker == True:
        i = i + 1
        squareSeq.append(squareSeq[i] + squareSeq[1] - squareSeq[0] + 8*i)
        if i + 2 == tup_num[2]:
            checker = False

    return squareSeq

sum(squareSeq((1, 5, 501))) + sum(squareSeq((1, 3, 501))) + sum(squareSeq((1, 9, 501))) + sum(squareSeq((1, 7, 501))) - 3
