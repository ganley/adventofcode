import sys

from operator import itemgetter
from parse import parse


def parse_ingredients(line):
    parsed = parse("{ingredients} (contains {allergens})", line)
    ingredients = parsed["ingredients"].split()
    allergens = parsed["allergens"].split(", ")
    return (ingredients, allergens)


# return a dict of encrypted ingredients to plaintext allergens
def analyze(ings):
    # build a dict whose keys are allergens, and whose values are the set
    # of all ingredients that appear in every list containing that allergen
    d = {}
    for ing, al in ings:
        for a in al:
            if a in d:
                d[a] = d[a].intersection(set(ing))
            else:
                d[a] = set(ing)

    # reduce the lists by repeatedly eliminating those for which there is
    # only one choice from the other lists in which they appear
    m = {}
    while sum([len(x) for x in d.values()]) > 0:
        singletons = {list(v)[0]: k for k, v in d.items() if len(v) == 1}
        m = {**m, **singletons}    # in Python 3.9 this will be m |= singletons
        s = set(singletons.keys())
        d = {k: v.difference(s) for k, v in d.items()}

    return m


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        ings = [parse_ingredients(line) for line in f]

    m = analyze(ings)

    # part 1: count of ingredients that aren't allergens
    print("Part 1:",
          sum([len([x for x in i if x not in m.keys()]) for i, _ in ings]))

    # part 2: encrypted allergens sorted by their plaintext
    print("Part 2:",
          ",".join([x[0] for x in sorted(m.items(), key=itemgetter(1))]))
