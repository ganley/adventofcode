import sys

import intgrid


flashes = 0


def step(g):
    global flashes

    flash = intgrid.Grid(g.width, g.height)

    for x in range(g.width):
        for y in range(g.height):
            g.set(x, y, g.get(x, y) + 1)

    progress = True
    while progress:
        progress = False
        ng = intgrid.Grid()
        ng.copy(g)
        for x in range(ng.width):
            for y in range(ng.height):
                if ng.get(x, y) > 9 and not flash.get(x, y):
                    flashes += 1
                    flash.set(x, y, 1)
                    n = ng.neighbors(x, y)
                    for nx, ny in n:
                        ng.set(nx, ny, ng.get(nx, ny) + 1)
                    progress = True
        g = ng

    for x in range(g.width):
        for y in range(g.height):
            if g.get(x, y) > 9:
                g.set(x, y, 0)

    return g


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = intgrid.Grid()
        g.read(f)

        for _ in range(100):
            g = step(g)

        print(flashes)
