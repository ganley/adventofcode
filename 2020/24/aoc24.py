import copy
import re
import sys

from hexgrid import HexGrid


def parse_dirs(txt):
    regex = re.compile("e|w|se|sw|ne|nw")
    parsed = []
    while txt:
        m = regex.match(txt).group(0)
        parsed.append(m)
        txt = txt[len(m):]
    return parsed


def dirs_to_coords(dirs):
    x, y = 0, 0
    for d in dirs:
        dx, dy = {
            "e": (2, 0),
            "ne": (1, 1),
            "nw": (-1, 1),
            "w": (-2, 0),
            "sw": (-1, -1),
            "se": (1, -1)
        }[d]
        x += dx
        y += dy
    return (x, y)


def iterate(grid):
    newgrid = HexGrid()
    for c, v in grid.grid.items():
        x, y = c

        # check black tiles
        if v == "b":
            n = grid.neighbors(x, y, "w")
            if n.get("b", 0) in [0, 3, 4, 5, 6]:
                newgrid.set(x, y, "w")
            else:
                newgrid.set(x, y, "b")

        # check white tiles. we have to check the neighbors of all of the
        # black tiles, because some white tiles won't be explicitly stored in
        # the HexGrid
        for dx, dy in HexGrid.deltas:
            nx = x + dx
            ny = y + dy
            # we always set the tile, so if it's set then it's already done
            if grid.get(nx, ny, "w") == "w" and not newgrid.get(nx, ny):
                n = grid.neighbors(nx, ny, "w")
                newgrid.set(nx, ny, "b" if n.get("b") == 2 else "w")

    return newgrid


def run(grid, num_iter):
    for i in range(num_iter):
        grid = iterate(grid)
    return grid.count("b")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        tiles = [parse_dirs(line.strip()) for line in f]

    # part 1
    floor = HexGrid()
    for t in tiles:
        x, y = dirs_to_coords(t)
        if floor.get(x, y, "w") == "w":
            floor.set(x, y, "b")
        else:
            floor.set(x, y, "w")
    print("Part 1:", floor.count("b"))

    # part 2
    nb = run(floor, 100)
    print("Part 2:", nb)
