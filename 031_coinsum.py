def coinsum():
    '''Calculate and return the number of possible combinations to get two pounds.
    '''

    counter = 0

    for pn2 in range(0, 1 + 1):
        for pn1 in range(0, 2 + 1):
            for p50 in range(0, 4 + 1):
                for p20 in range(0, 10 + 1):
                    for p10 in range(0, 20 + 1):
                        for p5 in range(0, 40 + 1):
                            for p2 in range(0, 100 + 1):
                                for p1 in range(0, 200 + 1):
                                    if p1 + 2 * p2 + 5 * p5 + 10 * p10 + 20 * p20 + 50 * p50 + 100 * pn1 + 200 * pn2 == 200:
                                        counter += 1

    print(counter)
    return counter

coinsum()