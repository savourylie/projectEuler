def reciCycle(num):
    """ (int) -> int

    Return the number of digit numbers of the reciprocal cycle of 1/num.
    
    >>> reciCycle(6)
    1
    >>> reciCycle(7)
    6
    >>> reciCycle(10)
    0
    """

    target = 1/num
    s_target = str(target)
    target_list = []
    counter_dict = {}
    counter = 0
    
    for index in range(2, len(s_target)):
        if s_target[index] not in target_list:
            target_list.append(s_target[index])
            counter_dict[s_target[index]] = 0
            counter_dict[s_target[index]] = counter_dict[s_target[index]] + 1
        elif counter_dict[s_target[index]] == 1:
            counter_dict[s_target[index]] = counter_dict[s_target[index]] + 1

    for word in counter_dict:
        if counter_dict[word] == 2:
            counter = counter + 1

    return counter

compareDummy = 0
noter = 0
            
for d in range(1, 1000):
    if reciCycle(d) > compareDummy:
        compareDummy = reciCycle(d)
        noter = d

print(noter)
    
