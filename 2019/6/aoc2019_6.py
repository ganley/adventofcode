import networkx as nx
import sys


def path(G, n):
    p = [n]
    while True:
        parent = list(G.successors(n))
        if not parent:
            return p
        p.append(parent[0])
        n = parent[0]


if __name__ == "__main__":
    G = nx.DiGraph()
    with open(sys.argv[1], "r") as f:
        for line in f:
            t = line.strip().split(")")
            G.add_edge(t[1], t[0])

    print("Part 1:", sum([len(path(G, n)) - 1 for n in G.nodes]))

    a_me = path(G, "YOU")
    a_santa = path(G, "SAN")
    for i, a in enumerate(a_me):
        if a in a_santa:
            print("Part 2:", i + a_santa.index(a) - 2)
            sys.exit(0)
