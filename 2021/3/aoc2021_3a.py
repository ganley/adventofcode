import sys


if __name__ == "__main__":
    inp = []
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                inp.append(line)

    bits = len(inp[0])
    counts = []
    n = len(inp) // 2
    for i in range(bits):
        counts.append(sum([int(b[i]) for b in inp]))

    gamma = 0
    epsilon = 0
    for c in counts:
        gamma *= 2
        if c >= n:
            gamma += 1
        epsilon *= 2
        if c < n:
            epsilon += 1

    print(f'{gamma=} {epsilon=} product={gamma*epsilon}')

