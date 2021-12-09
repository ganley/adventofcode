import sys

import intgrid


if __name__ == "__main__":
    g = intgrid.Grid()
    with open(sys.argv[1], "r") as f:
        g.read(f)

    risk = 0
    for x in range(g.width):
        for y in range(g.height):
            if (v := g.get(x, y)) < min([g.get(n[0], n[1]) for n in g.neighbors(x, y)]):
                risk += 1 + v

    print(risk)
