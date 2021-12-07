import math
import sys


def cost(x, p):
    c = 0
    for xi in x:
        # cost for part 1
        #c += abs(xi - p)

        # cost for part 2
        d = abs(xi - p) + 1
        c += d * (d - 1) // 2
    return c


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                x = [int(p) for p in line.split(',')]
                break

    mincost = max(x) * max(x) * len(x)   # greater than possible
    minp = -1
    for p in range(min(x), max(x) + 1):
        c = cost(x, p)
        if c < mincost:
            mincost = c
            minp = p

    assert minp != -1
    print(f'pos={minp} cost={cost(x, minp)}')
