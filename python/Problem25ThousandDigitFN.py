def fibonacci(num):
    """ (int) -> int

    Return the numth Fibonacci number.
    
    >>> fibonacci(6)
    8
    >>> fibonacci(12)
    144    
    """

    fib_list = [1, 1]

    for i in range(2, num):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        
    return fib_list[num - 1]
    
checker = False
term = 0

while checker == False:
    term = term + 1
    if len(str(fibonacci(term))) == 1000:
        checker = True
    
print(term)    
