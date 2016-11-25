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
    return (get_fibonacci((n+2)%60) - 1)

def fibonacci_partial_sum_fast(from_, to):
    return (fibonacci_sum_fast(to) - fibonacci_sum_fast(from_ - 1)) % 10

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    f = open('cases.txt')
    for line in f:
        from_, to = map(int, line.split())
        result_naive = fibonacci_partial_sum_naive(from_, to)
        result_fast = fibonacci_partial_sum_fast(from_, to)
        print(result_naive == result_fast)
