from collections import Counter
import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    layers = []
    while inp:
        layers.append(inp[:150])
        inp = inp[150:]

    # part 1
    least0s = 25 * 6
    prod12 = 0
    for layer in layers:
        c = Counter(list(layer))
        if c["0"] < least0s:
            least0s = c["0"]
            prod12 = c["1"] * c["2"]
    print(f"Part 1: {prod12}\n")

    # part 2
    print("Part 2:")
    for px in range(25 * 6):
        ps = [layer[px] for layer in layers]
        v = [p for p in ps if p != "2"][0]      # topmost non-2 value
        sys.stdout.write("." if v == "0" else "#")
        if px % 25 == 24:
            sys.stdout.write("\n")
