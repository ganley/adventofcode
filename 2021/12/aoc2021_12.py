# this prints the paths; use `wc -l` to count them

import sys


def is_small(v):
    return v == v.lower()


def paths(g, v, path, visited, twice):
    if v == 'end':
        print(f'{path + ["end"]}')
        return
    if is_small(v) and v in visited:
        if twice or v == 'start' or v == 'end':
            return
        else:
            twice = True
    
    for e in g[v]:
        paths(g, e, path + [v], visited + [v], twice)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = {}
        for rawline in f:
            if line := rawline.strip():
                u, v = line.split('-')
                g[u] = g.get(u, []) + [v]
                g[v] = g.get(v, []) + [u]

    #paths(g, 'start', [], [], True)      # part 1
    paths(g, 'start', [], [], False)     # part 2

