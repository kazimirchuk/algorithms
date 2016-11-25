# Uses python3
import sys

def optimal_weight_dynamic(knapsackCapacity, goldBars):
    value = []
    for k in range(0, knapsackCapacity + 1):
        row = []
        for m in range(0, len(goldBars)):
            row.append(0)
        value.append(row)

    for i in range(0, len(goldBars)):
        for j in range(0, knapsackCapacity + 1):
            value[j][i] = value[j][i - 1]
            if goldBars[i] <= j:
                val = value[j - goldBars[i]][i-1] + goldBars[i]
                if value[j][i] < val:
                    value[j][i] = val

    return value[knapsackCapacity][len(goldBars)-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_dynamic(W, w))
