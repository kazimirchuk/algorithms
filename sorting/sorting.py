# Uses python3
import sys
import random

def partition3Fast(a, l, r):
    pivot = a[l]
    lastPivotIndex = l
    firstPivotIndex = l
    for i in range(lastPivotIndex + 1, r + 1):
        if a[i] == pivot:
            lastPivotIndex += 1
            a[lastPivotIndex], a[i] = a[i], a[lastPivotIndex]
        if a[j] < pivot:
            lastPivotIndex += 1
            a[j], a[lastPivotIndex] = a[lastPivotIndex], a[j]
            a[lastPivotIndex], a[firstPivotIndex] = a[firstPivotIndex], a[lastPivotIndex]
            firstPivotIndex += 1

    return [firstPivotIndex, lastPivotIndex]

# def partition3Fast(a, l, r):
#     pivot = a[l]
#     lastPivotIndex = l
#     firstPivotIndex = l
#     for i in range(lastPivotIndex + 1, r + 1):
#         if a[i] == pivot:
#             lastPivotIndex += 1
#             a[lastPivotIndex], a[i] = a[i], a[lastPivotIndex]
#
#     for j in range(lastPivotIndex + 1, r + 1):
#         if a[j] < pivot:
#             lastPivotIndex += 1
#             a[j], a[lastPivotIndex] = a[lastPivotIndex], a[j]
#             a[lastPivotIndex], a[firstPivotIndex] = a[firstPivotIndex], a[lastPivotIndex]
#             firstPivotIndex += 1
#     return [firstPivotIndex, lastPivotIndex]

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition3Fast(a, l, r)
    if m[0] != 'none':
        randomized_quick_sort(a, l, m[0] - 1);
    if m[1] != 'none':
        randomized_quick_sort(a, m[1] + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
