import sys

from heapq import heappop, heappush

import intgrid


def astar(g, start, end):
    inf = 100000

    score = { start: 0 }
    parent = {}

    frontier = []
    heappush(frontier, (g.get(start[0], start[1]), start))
    while frontier:
        f, v = heappop(frontier)
        if v == end:
            c = 0
            p = end
            while p != start:
                c += g.get(p[0], p[1])
                p = parent.get(p)
            return c
        for n in g.neighbors(v[0], v[1]):
            s = score.get(v, inf) + g.get(n[0], n[1])
            if s < score.get(n, inf):
                parent[n] = v
                score[n] = s
                if n not in frontier:
                    heappush(frontier, (s, n))

    return None



# 9 wraps to 1 ... there's surely a numerical way to do this
def wrap(n):
    if n > 9:
        n -= 9
    return n


def make_detailed_grid(g):
    h = intgrid.Grid(g.width * 5, g.height * 5)
    for i in range(5):
        for j in range(5):
            for x in range(g.width):
                for y in range(g.height):
                    h.set(x + i * g.width, y + j * g.height,
                          wrap(g.get(x, y) + i + j))

    return h


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = intgrid.Grid()
        g.read(f)

    g = make_detailed_grid(g)     # part 2 only

    p = astar(g, (0, 0), (g.width - 1, g.height - 1))

    print(p)
