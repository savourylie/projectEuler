def collatz(num):
    """ (int) -> int

    Return the length of the Collatz chain of num.
    
    >>> collatz(13)
    10
    >>> collatz(60)
    20
    """

    checker = False
    n = num
    result = 0
    result_list = []
    
    while checker == False:

        if n == 1:
            checker = True
            
        result = n
        result_list.append(result)
        
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0 and n != 1:
            n = 3*n + 1
            
    if num == 0:
        return "The parameter can't be 0!"
    else:
        return len(result_list)


def checkCollatz(num):
    """ (int) -> [int, int]

    Return the length of the longest Collatz chain under num
    and the number that produces it, in the form of
    [length, number].
    
    >>> checkCollatz(5)
    [8, 3]
    >>> checkCollatz(10)
    [20, 9]
    """

    checker = False
    container = 0
    result_list = {}
    index = 1

#Need to put all the length of Collatz chains under num in
#the list for later comparison.
    
    for i in range(1, num + 1):
        result_list[i] = collatz(i)

#Find the maximum value in the dictionary.
        
    for word in result_list:
        if result_list[word] > container:
            container = result_list[word]
    
    while checker == False and index in range(len(result_list)):
        if container == result_list[index]:
            checker = True
            index_r = index
        index = index + 1
        
    return [container, index_r]
