import math
import sys


def calculate_fuel(mass):
    fuel = max(int(math.floor(mass / 3)) - 2, 0)
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    return fuel


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        values = [int(line) for line in f]

    total = 0
    for mass in values:
        fuel = calculate_fuel(mass)
        print(f"{mass=} {fuel=}")
        total += fuel

    print(f"{total=}")
