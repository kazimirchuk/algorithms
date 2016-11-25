# Uses python3

import sys

def get_key(item):
    return item[0]

def get_optimal_value(capacity, weights, values):
    value = 0.
    loots = []

    for v, w in zip(values, weights):
        loots.append([v/w, v, w])

    for loot in (sorted(loots, reverse=True, key=get_key)):
        if capacity == 0:
            return value
        else:
            w = loot[2]
            v = loot[1]
            vw = loot[0]
            if w <= capacity:
                capacity -= w
                value += v
            else:
                value += (vw * capacity)
                capacity = 0

    else:
        return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
