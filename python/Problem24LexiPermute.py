import random
import math
import itertools

def permute(num_str):
    """ (str of int) -> list of str

    Return all of the permutations of the digits from num_list in
    lexicographic order.
    
    >>> permute('012')
    ['012', '021', '102', '120', '201', '210']
    >>> permute('01')
    ['01', '10']
    """

    perms = [''.join(p) for p in itertools.permutations(num_str)]

    return perms

def numth_perm(perm, num):
    """ (list of str of int) -> int

    Return the numth permutations of the given list.

    >>> numth_perm('012', 5)
    '201'
    """

    int_perm = []
    perms = permute(perm)
    
    for p in perms:
        int_perm.append(int(p))
   
    return sorted(int_perm)[num - 1]
