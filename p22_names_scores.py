import csv

def alpha_to_num(string):
    from string import ascii_uppercase

    alpha_to_num_dict = {k: ord(k) - 64 for k in ascii_uppercase}
    return sum([alpha_to_num_dict.get(x) for x in string])

def main():
    with open('names.txt', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        name_list = list(reader)[0]

    name_list_sorted = sorted(name_list)

    num_list_sorted = list(map(alpha_to_num, name_list_sorted))
    pos_list = [i + 1 for i in range(len(num_list_sorted))]

    mul_list = [num_list_sorted[i] * pos_list[i] for i in range(len(num_list_sorted))]
    summation = sum(mul_list)
    print(summation)

if __name__ == '__main__':
    main()