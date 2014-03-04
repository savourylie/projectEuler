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

#Find out all the amicable numbers under 10000.

def amicable(num):
    """ (int) -> list of int

    Return all the amicable numbers under num.
    
    """

    result_dict = {}
    result_list = []
    
    for number in range(1, num+1):
        result_dict[number] = d(number)

    for word in result_dict:
        if result_dict[word] in result_dict:
            if result_dict[result_dict[word]] == word:
                if word not in result_list and word != result_dict[word]:
                    result_list.append(word)

    return result_list
        
