# Uses python3
import sys

def get_change(m):
    n = 0
    count = 0
    coins = [10, 5, 1]

    while n != m:
        for i, coin in enumerate(coins):
            while (m - n) >= coin:
                n += coin
                count += 1

    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
