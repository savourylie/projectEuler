def numToWord1_19(num):
    """ (int) -> str

    Return the int written out in words, range from 1 to 19.
    
    >>> numToWord(9)
    'nine'
    >>> numToword(7)
    'seven'
    >>> numToWord(16)
    'sixteen'
    >>> numToword(12)
    'twelve'
    """

    word = ''
    numSum = 0
    
    if num == 1:
        word = 'one'
    if num == 2:
        word = 'two'
    if num == 3:
        word = 'three'
    if num == 4:
        word = 'four'
    if num == 5:
        word = 'five'
    if num == 6:
        word = 'six'
    if num == 7:
        word = 'seven'
    if num == 8:
        word = 'eight'
    if num == 9:
        word = 'nine'
    if num == 10:
        word = 'ten'
    if num == 11:
        word = 'eleven'
    if num == 12:
        word = 'twelve'
    if num == 13:
        word = 'thirteen'
    if num == 14:
        word = 'fourteen'
    if num == 15:
        word = 'fifteen'
    if num == 16:
        word = 'sixteen'
    if num == 17:
        word = 'seventeen'
    if num == 18:
        word = 'eighteen'
    if num == 19:
        word = 'nineteen'   

    return word

def numToWord(num):
    """ (int) -> str

    Return the int written out in words, below 1000.
    
    >>> numToWord(359)
    'threehundredandfiftynine'
    >>> numToWord(709)
    'sevenhundredandnine'
    >>> numToWord(96)
    'nintysix'
    >>> numToWord(1000)
    'onethousand'
    """

    word = ''

    decs = {}

    decs[20] = 'twenty'
    decs[30] = 'thirty'
    decs[40] = 'forty'
    decs[50] = 'fifty'
    decs[60] = 'sixty'
    decs[70] = 'seventy'
    decs[80] = 'eighty'
    decs[90] = 'ninety'

    hundreds = {}

    hundreds[100] = 'onehundred'
    hundreds[200] = 'twohundred'
    hundreds[300] = 'threehundred'
    hundreds[400] = 'fourhundred'
    hundreds[500] = 'fivehundred'
    hundreds[600] = 'sixhundred'
    hundreds[700] = 'sevenhundred'
    hundreds[800] = 'eighthundred'
    hundreds[900] = 'ninehundred'
    hundreds[1000] = 'onethousand'
    
    if num in range(20):
        word = numToWord1_19(num)
    
    if num in range(20, 100):
        word = decs[num - num%10] + numToWord1_19(num%10)

    if num in range(100, 1001):
        if num % 100 == 0:
            if num == 1000:
                word = hundreds[1000]
            else:
                word = hundreds[(num//100)*100]
        else:
            word = numToWord1_19(num//100) + 'hundredand' + numToWord(num%100)
    

    return word

def sumWords(num):
    """ (int) -> int

    Return the number of letters used counting from 1 to num, below 1000.
    
    >>> sumWords(5)
    19
    >>> sumWords(9)
    31
    """

    nLetterSum = 0
    
    for i in range(1, num + 1):
        nLetterSum = nLetterSum + len(numToWord(i))

    return nLetterSum
