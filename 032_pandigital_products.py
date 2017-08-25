from collections import Counter
import numpy as np

def pandigital_checker(string):
    """Return True iff string contains 1-9 only once.
    """
    # Check length
    if len(string) != 9:
        return False

    # Break string into list
    string_list = list(string)

    # Filter out that ZERO
    if '0' in string_list:
        return False

    # Count the occurrences with Counter
    string_count = Counter(string_list)

    # Check uniqueness
    if len(set(string_count)) != 9:
        return False

    return True


def main():
    """Check combinations
    """
    result_list = []

    # 1 and (3) 4 Combinations
    for d in range(1, 10):
        for dddd in range(100, 10000):
            prod = d * dddd
            candidate1 = str(d) + str(dddd) + str(prod)
            candidate2 = str(dddd) + str(d) + str(prod)

            if pandigital_checker(candidate1):
                result_list.append(candidate1)

            if pandigital_checker(candidate2):
                result_list.append(candidate2)

    # 2 and (2) 3 Combinations
    for dd in range(10, 100):
        for ddd in range(10, 1000):
            prod = dd * ddd
            candidate1 = str(dd) + str(ddd) + str(prod)
            candidate2 = str(ddd) + str(dd) + str(prod)

            if pandigital_checker(candidate1):
                result_list.append(candidate1)

            if pandigital_checker(candidate2):
                result_list.append(candidate2)

    print(set(result_list))

    print(np.sum([1, 2, 3]))

    return np.sum(list(map(int, list(set(result_list)))))

print(main())
