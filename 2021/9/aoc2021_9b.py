import sys

import intgrid


def get_basin(g, x, y, visited):
    if (x, y) in visited or g.get(x, y) == 9:
        return []
    visited.append((x, y))
    b = [(x, y)]
    for n in g.neighbors(x, y):
        b += get_basin(g, n[0], n[1], visited)
    return b


if __name__ == "__main__":
    g = intgrid.Grid()
    with open(sys.argv[1], "r") as f:
        g.read(f)

    risk = 0
    visited = []
    basin_sizes = []
    for x in range(g.width):
        for y in range(g.height):
            if (v := g.get(x, y)) < min([g.get(nx, ny) for (nx, ny) in g.neighbors(x, y)]):
                b = get_basin(g, x, y, visited)
                basin_sizes.append(len(b))

    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
