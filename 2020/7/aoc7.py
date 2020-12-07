import sys

# parent (downward): parent color -> { child_color: n }
# child (upward): child color ->  { parent color : n }

# returns (parent graph, child graph)
def build_graph(filename):
    with open(filename, "r") as f:
        child = {}
        parent = {}
        for line in f:
            tok = line.split()
            parentcolor = tok.pop(0) + "_" + tok.pop(0)
            assert tok.pop(0) == "bags" and tok.pop(0) == "contain"

            assert not parentcolor in parent
            parent[parentcolor] = {}

            while tok:
                numstr = tok.pop(0)
                if num := 0 if numstr == "no" else int(numstr):
                    childcolor = tok.pop(0) + "_" + tok.pop(0)
                    parent[parentcolor][childcolor] = num
                else:
                    childcolor = tok.pop(0)
                    assert childcolor == "other"

                assert (num == 0 and childcolor == "other") or num > 0
                assert tok.pop(0).startswith("bag")

                if childcolor != "other":
                    if not childcolor in child:
                        child[childcolor] = {}
                    child[childcolor][parentcolor] = num

    return (parent, child)



def ancestors(childgraph, color):
    anc = []
    for parentcolor in childgraph.get(color, {}):
        anc.append(parentcolor)
        anc += ancestors(childgraph, parentcolor)
    return list(set(anc))



# do *not* count the outermost bag
def total_bags_contained(parentgraph, color):
    weight = 0
    for childcolor,w in parentgraph.get(color, {}).items():
        weight += w
        weight += w * total_bags_contained(parentgraph, childcolor)
    return weight



parentgraph,childgraph = build_graph(sys.argv[1])

# part 1:
print(len(ancestors(childgraph, "shiny_gold")))

# part 2:
print(total_bags_contained(parentgraph, "shiny_gold"))

