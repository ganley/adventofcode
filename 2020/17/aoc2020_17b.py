import sys

from grid4d import Grid


def iterate(grid):
    newgrid = Grid()
    xs = [coord[0] for coord in grid.grid]
    minx, maxx = min(xs), max(xs)
    ys = [coord[1] for coord in grid.grid]
    miny, maxy = min(ys), max(ys)
    zs = [coord[2] for coord in grid.grid]
    minz, maxz = min(zs), max(zs)
    ws = [coord[3] for coord in grid.grid]
    minw, maxw = min(ws), max(ws)
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                for w in range(minw - 1, maxw + 2):
                    v = grid.get(x, y, z, w, ".")
                    n = grid.neighbors(x, y, z, w)
                    if v == "#" and 2 <= n.get("#", 0) <= 3:
                        newgrid.set(x, y, z, w, "#")
                    elif v == "." and n.get("#", 0) == 3:
                        newgrid.set(x, y, z, w, "#")
    return newgrid


def run(grid):
    for i in range(6):
        newgrid = iterate(grid)
        print(f"{i=}")
        grid = newgrid
    return grid.count("#")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        grid = Grid()
        grid.read(f, empty_state=".")

    print(run(grid))
