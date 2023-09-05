def circularNum(num):
    """ (int) -> list of int

    Return all the circular numbers of num in a list.
    
    >>> circularNum(123)
    [123, 231, 312]
    >>> circularNum(12569)
    [12569, 25691, 56912, 69125, 91256]
    """

    s_num = str(num)
    buffer = s_num[0]
    checker = True
    n_num = ''
    result_list = [num]
    
    while checker == True:
        for i in range(0, len(s_num) - 1):
            n_num = n_num + s_num[i+1]
        n_num = n_num + buffer
        n_num = int(n_num)
        
        if n_num not in result_list:
            result_list.append(n_num)
        else:
            checker = False

        s_num = str(n_num)
        buffer = s_num[0]
        n_num = ''
        
    return result_list

def prime(num):
    """ (int) -> bool

    Return True if num is a prime and False otherwise.

    >>> prime(10)
    False
    >>> prime(228)
    False
    >>> prime(37)
    True
    """

    test = True
    result = []
    j = 2

    while (j < num and test == True):
        if num % j == 0:
            test = False
        else:
            j = j + 1

    if num == 0 or num == 1:
        test = False
        
    return test

def isCircularPrime(num):        
    """ (int) -> bool

    Return True if num is a circular prime and False is otherwise.
    
    >>> isCircularPrime(79)
    True
    >>> isCircularPrime(37)
    True
    >>> isCircularPrime(23)
    False
    """
    
    c_num_list = circularNum(num)
    checker = True
    
    for i in range(len(c_num_list)):
        if prime(c_num_list[i]) == False:
            checker = False

    return checker

def findTheNumber(num):
    """ int -> [int, list of int]

    Return the number of circular primes under num and list out all the numbers.
    
    >>> findTheNumber(100)
    [13, [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]]
    """

    result_list = []
    
    for i in range(num):
        if isCircularPrime(i) == True:
            result_list.append(i)
            
        if i/num in [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]:
            print(str((i/num)*100) + '%')
    
    return [len(result_list), result_list]

# The result is data_list. However, any numbers with digit 0 doesn't count
# in this case so need to remove all of them using the following code.


##data_list = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 101, 103, 107, 113, 131, 197, 199, 307, 311, 337, 373, 701, 709, 719, 733, 907, 919, 971, 991, 1013, 1031, 1097, 1103, 1193, 1301, 1931, 3001, 3011, 3037, 3119, 3779, 7001, 7019, 7109, 7793, 7937, 9007, 9091, 9311, 9377, 10007, 10099, 10103, 10193, 10301, 10909, 11939, 13001, 19391, 19937, 30011, 30119, 31019, 37199, 39119, 70001, 70003, 70009, 70019, 70793, 70937, 71993, 77093, 90007, 90019, 90071, 91009, 91193, 93719, 93911, 97001, 99371, 100003, 100103, 100193, 100931, 101939, 103001, 109391, 109937, 110939, 193939, 199933, 300007, 300073, 300119, 300779, 307079, 310019, 319993, 331999, 390119, 391939, 393919, 700001, 700109, 700303, 700937, 900007, 900019, 900091, 900701, 901009, 901193, 909371, 919393, 930011, 930077, 930707, 933199, 939011, 939193, 939391, 990001, 993319, 999331]
##
##new_list = list(data_list)
##
##for i in data_list:
##
##    checker = True
##    num = i
##    s_num = str(i)
##
##    for j in range(len(s_num)):
##        digit = (num // 10**j) % 10
##        if digit == 0:
##            checker = False
##
##    if checker == False:
##        new_list.remove(num)

