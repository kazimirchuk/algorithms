# Uses python3

import sys
import re
import math

def get_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibonacci_sum_fast(n):
    return (get_fibonacci((n+2)%60) - 1) % 10

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    f = open('cases.txt')
    input = f.read()
    cases = input.split()
    for i in range(len(cases)):
        cases[i] = int(cases[i])
        result_naive = fibonacci_sum_naive(cases[i])
        result_fast = fibonacci_sum_fast(cases[i])
        print(result_naive == result_fast)
