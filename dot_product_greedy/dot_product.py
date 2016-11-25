#Uses python3

import sys

def max_dot_product(a, b):
    res = 0
    a.sort()
    b.sort()

    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    f = open('cases.txt')
    for line in f:
        case = line.split()
        for c in range(len(case)):
            case[c] = int(case[c])
        n = case[0]
        a_numbers = case[1:n + 1]
        b_numbers = case[n+1:len(case) + 1]

        print(max_dot_product(a_numbers, b_numbers))
