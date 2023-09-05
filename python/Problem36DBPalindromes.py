def biToDec(num):
    """ (int) -> int

    Return the binary form of num.
    
    >>> biToDec(1010)
    1111110010
    >>> biToDec(1058)
    10000100010
    >>> biToDec(17)
    10001
    """

    dividend = num
    remainder = 0
    result_list = []
    
    while dividend != 0:
        remainder = dividend%2
        dividend = dividend//2
        result_list.append(remainder)

    result_list.reverse()

    result_str = ''
    
    for i in range(len(result_list)):
        result_str = result_str + str(result_list[i])

    if result_str == '':
        result = 0
        
    else:
        result = int(result_str)
    
    return result

def intReverse(num):
    """ (int) -> int

    Return the reverse number of num.
    
    >>> intReverse(581)
    185
    >>> intReverse(9686)
    6869
    >>> intReverse(9)
    9
    """

    s_num = str(num)
    list_num = []

    for i in s_num:
        list_num.append(i)

    list_num.reverse()

    s_reverse_num = ''

    for i in range(len(list_num)):
        s_reverse_num = s_reverse_num + list_num[i]

    reverse_num = int(s_reverse_num)

    return reverse_num

def findTheNumber(num):
    """ (int) -> list of int

    Return all the palindromic numbers that are palindromic in base 10 and base 2,
    under num.

    >>> findTheNumber(10)
    [0, 1, 3, 5, 7, 9]
    """

    result_list = []
    
    for i in range(num):
        if i == intReverse(i) and biToDec(i) == intReverse(biToDec(i)):
            result_list.append(i)
            
        if i/num in [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]:
            print(str((i/num)*100) + '%')
            
    return result_list
