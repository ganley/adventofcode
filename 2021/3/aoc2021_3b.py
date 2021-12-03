import sys


if __name__ == "__main__":
    # read input
    inp = []
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                inp.append(line)

    saveinp = inp  # saved for second pass

    # do gamma
    bits = len(inp[0])
    for i in range(bits):
        ones = sum([int(b[i]) for b in inp])
        n = len(inp)
        zeros = n - ones

        newinp = []
        for x in inp:
            if (ones < zeros and x[i] == '0') or (ones >= zeros and x[i] == '1'):
                newinp.append(x)
        inp = newinp
        if len(inp) == 1:
            break

    assert len(inp) == 1
    gamma = int(inp[0], 2)

    # do epsilon
    inp = saveinp
    for i in range(bits):
        ones = sum([int(b[i]) for b in inp])
        n = len(inp)
        zeros = n - ones

        newinp = []
        for x in inp:
            if (zeros <= ones and x[i] == '0') or (zeros > ones and x[i] == '1'):
                newinp.append(x)
        inp = newinp
        if len(inp) == 1:
            break

    assert len(inp) == 1
    epsilon = int(inp[0], 2)

    print(f'{gamma=} {epsilon=} product={gamma*epsilon}')
