import itertools
import math
import sys


# list of differences between adjacent pairs of elements
def deltas(adapters):
    return [(b - a) for a, b in zip(adapters, adapters[1:])]


# returns ( number of 1 diffs, number of 3 diffs)
def collate_deltas(adapters):
    d = deltas(adapters)
    return (d.count(1), d.count(3))


# for a chain of length x, the number of subchains with at most 2 removed
def count_subchains(x):
    return 1 + x + math.comb(x, 2)


# given a list of adapters, return a list of the lengths of the streaks of
# consecutive adapters that are 1 jolt from the next-lower one
def streaks(adapters):
    return [len(list(x[1]))
            for x in itertools.groupby(deltas(adapters)) if x[0] == 1]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        adapters = sorted([int(line) for line in f])

    # add sentinels
    adapters = [0] + adapters + [adapters[-1] + 3]

    # part 1
    one, three = collate_deltas(adapters)
    print(f"Part 1: {one} * {three} = {one * three}")

    # part 2
    m = math.prod(count_subchains(x - 1) for x in streaks(adapters))
    print(f"Part 2: {m}")
