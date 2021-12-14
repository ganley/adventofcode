import collections
import operator
import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        template = ''
        rules = {}
        for rawline in f:
            if line := rawline.strip():
                if template:
                    t = line.split('->')
                    rules[t[0].strip()] = t[1].strip()
                else:
                    template = line
            else:   # blank line
                assert template

    for _ in range(10):
        pairs = zip(list(template), list(template)[1:])
        new = ''
        for a, b in pairs:
            new += a + rules[''.join([a, b])]
        new += b
        template = new

    c = sorted(list(collections.Counter(template).items()), key=operator.itemgetter(1))

    print(c[-1][1] - c[0][1])
