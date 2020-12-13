import sys

# key observation here: from a timestamp that works for the first N buses,
# you can skip forward by the product of all N buses that work

# if successful, returns 0
# if unsuccessful, returns the product of the buses that worked
def check(x, buses):
    p = 1
    for i, b in enumerate(buses):
        if (x + i) % b != 0:
            return p
        p *= b
    return 0


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        tm_str, buses_str = [x for x in f.read().split()]
        tm = int(tm_str)
        buses = [1 if b == "x" else int(b) for b in buses_str.split(",")]

    n = [b for b in buses if b != 1]

    t = 0
    while True:
        print(f"checking {t=}")
        c = check(t, buses)
        if c == 0:
            print(t)
            sys.exit(0)
        t += c
