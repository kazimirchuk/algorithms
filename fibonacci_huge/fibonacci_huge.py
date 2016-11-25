# Uses python3

import sys
import re
import math

def get_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def get_pisano_period(n, m):
    period = [0, 1]
    i = 2
    while True:
        period.append((period[i-1] + period[i-2]) % m)
        period_length = len(period)
        if period_length % 2 == 0 and period_length != 0 and period[:int(period_length/2)] == period[int(period_length/2):]:
            break
        i += 1
    return period[:int(period_length/2)]

def get_fibonacci_huge(n, m):
    regexp = re.compile('^10*$')
    matched = regexp.match(str(m))
    if matched:
        pisano_period_length = 6 * m
    else:
        pisano_period_length = len(get_pisano_period(n, m))

    remainder = n % pisano_period_length
    return get_fibonacci(remainder) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
