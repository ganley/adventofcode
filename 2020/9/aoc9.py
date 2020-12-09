import sys


def find_bad(a):
    preamble = set(a[:25])
    for i, x in enumerate(a[25:], start=25):
        for h in preamble:
            d = x - h
            if d != h and d in preamble:
                break
        else:
            return x
        preamble.remove(a[i - 25])
        preamble.add(x)

    return None


# sliding window. expand to the right while sum is less than target, contract
# from the left if sum exceeds target. only works if all numbers are positive.
# returns a tuple of the start and end indices of the subarray.
def subset_sum(a, t):
    start_ix = 0
    curr_sum = a[0]
    for i, x in enumerate(a[1:], start=1):
        curr_sum += x
        while curr_sum > t:
            curr_sum -= a[start_ix]
            start_ix += 1
        if curr_sum == t:
            return (start_ix, i)
    return None


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        a = [int(x) for x in f.readlines()]

    # part 1
    bad = find_bad(a)
    print(f"part 1: {bad}")

    # part 2
    i, j = subset_sum(a, bad)
    subset = a[i:(j+1)]
    print(f"part 2: {min(subset) + max(subset)}")
