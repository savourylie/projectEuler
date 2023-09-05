def possibleComb():

    result_list = []

    for a in range(201):
        for b in range(101):
            for c in range(41):
                for d in range(21):
                    for e in range(11):
                        for f in range(5):
                            for g in range(3):
                                for h in range(2):
                                    if 0.01*a + 0.02*b + 0.05*c + 0.1*d + 0.2*e + 0.5*f + g + 2*h == 2:
                                        result_list.append([a, b, c, d, e, f, g, h])
                                        print([a, b, c, d, e, f, g, h])

    return len(result_list)
