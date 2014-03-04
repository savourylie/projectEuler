def powerDigitSum(num1, num2):
    """ (int, int) -> int

    Return the digit sum of num1 ** num2.

    >>> powerDigitSum(2, 15)
    26
    >>> powerDigitSum(3, 10)
    27
    """

    power = num1**num2
    s_power = str(power)
    digit = 0
    digitSum = 0

    for i in range(len(str(power))):
                   digit = (power // 10**i) % 10
                   digitSum = digitSum + digit

    return digitSum
    
