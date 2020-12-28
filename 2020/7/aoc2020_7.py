import sys

# parent (downward): parent_color -> { child_color: n }
# child (upward): child_color ->  { parent_color : n }

# returns (parent_graph, child_graph)


def build_graph(filename):
    with open(filename, "r") as f:
        child = {}
        parent = {}
        for line in f:
            tok = line.split()
            parent_color = tok.pop(0) + "_" + tok.pop(0)
            assert tok.pop(0) == "bags" and tok.pop(0) == "contain"

            assert parent_color not in parent
            parent[parent_color] = {}

            while tok:
                num_str = tok.pop(0)
                if num := 0 if num_str == "no" else int(num_str):
                    child_color = tok.pop(0) + "_" + tok.pop(0)
                    parent[parent_color][child_color] = num
                else:
                    child_color = tok.pop(0)
                    assert child_color == "other"

                assert (num == 0 and child_color == "other") or num > 0
                assert tok.pop(0).startswith("bag")

                if child_color != "other":
                    if child_color not in child:
                        child[child_color] = {}
                    child[child_color][parent_color] = num

    return (parent, child)


def ancestors(child_graph, color):
    anc = []
    for parent_color in child_graph.get(color, {}):
        anc.append(parent_color)
        anc += ancestors(child_graph, parent_color)
    return list(set(anc))


# do *not* count the outermost bag
def total_bags_contained(parent_graph, color):
    weight = 0
    for child_color, w in parent_graph.get(color, {}).items():
        weight += w
        weight += w * total_bags_contained(parent_graph, child_color)
    return weight


if __name__ == "__main__":
    parent_graph, child_graph = build_graph(sys.argv[1])

    # part 1:
    print(len(ancestors(child_graph, "shiny_gold")))

    # part 2:
    print(total_bags_contained(parent_graph, "shiny_gold"))
