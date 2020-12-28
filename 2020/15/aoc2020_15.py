import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        nums = [int(x) for x in f.read().split(",")]

    # ts0 is the timestamp of the most recent time the number was said
    # ts1 is the second-most-recent
    ts0 = {n: t for t, n in enumerate(nums)}
    ts1 = {}

    t = len(nums)   # timestamp
    say = nums[-1]
    while True:
        if say in ts0 and say not in ts1:
            say = 0
        else:
            say = ts0[say] - ts1[say]
        if say in ts0:
            ts1[say] = ts0[say]
        ts0[say] = t
        t += 1

        if t == 2020:
            print("Part 1:", say)

        if t == 30000000:
            print("Part 2:", say)
            sys.exit(0)
