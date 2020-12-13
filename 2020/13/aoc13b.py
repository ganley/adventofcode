from functools import reduce
import math
import sys


# the next two functions came from Rosetta Code
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

# this finds a value x such that x % a[i] == n[i] for all i
def chinese_remainder(n, a):
    total = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        tm_str, buses_str = [x for x in f.read().split()]
        tm = int(tm_str)
        buses = [1 if b == "x" else int(b) for b in buses_str.split(",")]

    n = [b for b in buses if b != 1]
    a = [0] + [(b - i) for i, b in enumerate(buses[1:], start=1) if b != 1]

    print(chinese_remainder(n, a))
