import sys


def check(n):
    digits = [int(c) for c in str(n)]
    diffs = [b - a for a,b in zip(digits, digits[1:])]
    return 0 in diffs and not [x for x in diffs if x < 0]


def check2(n):
    digits = [int(c) for c in str(n)]
    diffs = [b - a for a,b in zip(digits, digits[1:])]
    if not check(n):
        return False
    diffs = [1, 1] + diffs + [1, 1]
    for a,b,c in zip(diffs, diffs[1:], diffs[2:]):
        if a != 0 and b == 0 and c != 0:
            return True


if __name__ == "__main__":
    low = 123257
    high = 647015

    c1 = 0
    c2 = 0
    for i in range(low, high + 1):
        if check(i):
            c1 += 1
        if check2(i):
            c2 += 1

    print("Part 1:", c1)
    print("Part 2:", c2)
