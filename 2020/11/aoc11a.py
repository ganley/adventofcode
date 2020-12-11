from collections import Counter
import copy
import sys

from grid import Grid


def run(grid):
    newgrid = Grid()
    newgrid.copy(grid)
    for x in range(grid.width):
        for y in range(grid.height):
            v = grid.get(x, y)
            n = grid.neighbors(x, y)
            if v == "L" and "#" not in n or n.get("#") == 0:
                newgrid.set(x, y, "#")
            elif v == "#" and n.get("#", 0) >= 4:
                newgrid.set(x, y, "L")
    return newgrid


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        grid = Grid()
        grid.read(f, empty_state=".")

    while True:
        newgrid = run(grid)
        if newgrid == grid:
            print(grid.count("#"))
            sys.exit(0)
        grid = newgrid
