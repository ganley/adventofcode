import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        tm_str, buses_str = [x for x in f.read().split()]
        tm = int(tm_str)
        buses = [int(b) for b in buses_str.split(",") if b != "x"]

    t = tm
    while True:
        for b in buses:
            if t % b == 0:
                print(f"{t=} {b=}")
                answer = (t - tm) * b
                print(f"{answer=}")
                sys.exit(0)
        t += 1
