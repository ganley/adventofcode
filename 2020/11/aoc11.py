import sys

from grid import Grid


def iterate(grid, dist, thresh):
    newgrid = Grid()
    newgrid.copy(grid)
    for x in range(grid.width):
        for y in range(grid.height):
            v = grid.get(x, y)
            n = grid.neighbors(x, y, dist)
            if v == "L" and "#" not in n or n.get("#") == 0:
                newgrid.set(x, y, "#")
            elif v == "#" and n.get("#", 0) >= thresh:
                newgrid.set(x, y, "L")
    return newgrid


def run(grid, dist=1, thresh=4):
    while True:
        newgrid = iterate(grid, dist, thresh)
        if newgrid == grid:
            return grid.count("#")
        grid = newgrid


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        grid = Grid()
        grid.read(f, empty_state=".")

    print(f"Part 1: {run(grid, 1, 4)}")

    print(f"Part 2: {run(grid, 0, 5)}")
