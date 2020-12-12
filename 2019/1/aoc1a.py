import math
import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        values = [int(line) for line in f]

    total = 0
    for mass in values:
        fuel = int(math.floor(mass / 3)) - 2
        print(f"{mass=} {fuel=}")
        total += fuel

    print(f"{total=}")
