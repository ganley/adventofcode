import sys


if __name__ == "__main__":
    depths = []
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                depths.append(int(line))

    # next two lines for part 2 only
    s = zip(depths, depths[1:], depths[2:])
    depths = [ sum(x) for x in s ]

    incs = sum([b > a for a, b in zip(depths, depths[1:])])
    print(incs)
