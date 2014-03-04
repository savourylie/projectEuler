def gd5consect_numbers(number):
    """ (int) -> int

    Return the greatest product of five consecutive digits in number.

    >>> gd5consect_numbers(12345678935)
    15120
    >>> gd5consect_numbers(9998543521)
    29160
    """
    s_number = str(number)
    result_list = []

    for i in range(len(s_number)-4):
        result = int(s_number[i])*int(s_number[i+1])*int(s_number[i+2])*int(s_number[i+3])*int(s_number[i+4])
        result_list.append(result)

    m_result = max(result_list)

    return m_result
