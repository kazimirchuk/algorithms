# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    m1 = get_majority_element(a, left, (left + right - 1)//2 + 1)
    m2 = get_majority_element(a, (left + right - 1)//2 + 1, right)
    c1, c2 = 0, 0
    for i in range(left, right):
        if a[i] == m1:
            c1 += 1
        elif a[i] == m2:
            c2 += 1
    if c1 > (right-left)//2:
        return m1
    if c2 > (right-left)//2:
        return m2

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
