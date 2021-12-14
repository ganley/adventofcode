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

    p = [''.join(x) for x in zip(list(template), list(template)[1:])]
    pairs = collections.Counter(p)
  
    for _ in range(40):
        newpairs = {}
        for k, v in pairs.items():
            r = rules[k]
            p1 = k[0] + r
            p2 = r + k[1]
            newpairs[p1] = newpairs.get(p1, 0) + v
            newpairs[p2] = newpairs.get(p2, 0) + v
        pairs = newpairs

    # only count the first character in each pair, lest we count each
    # character twice. then add 1 more for the last character in the
    # original template (which is the last character in every template).
    c = {}
    for k, v in pairs.items():
        c[k[0]] = c.get(k[0], 0) + v
    c[template[-1]] = c.get(template[-1], 0) + 1

    c = sorted(list(c.items()), key=operator.itemgetter(1))

    print(c[-1][1] - c[0][1])
