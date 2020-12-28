import math
import sys


# parse the rule section
def parse_rules(txt):
    rules = {}
    for line in txt.split("\n"):
        c = line.split(":")
        fieldname = c[0]
        t = c[1].split()
        rule1 = tuple([int(x) for x in t[0].split("-")])
        assert t[1] == "or"
        rule2 = tuple([int(x) for x in t[2].split("-")])
        rules[fieldname] = (rule1, rule2)
    return rules


# parse a ticket section (used for both mine and nearby)
def parse_tickets(txt):
    tickets = []
    for line in txt.split("\n")[1:]:
        if line:
            t = [int(x) for x in line.split(",")]
            tickets.append(t)
    return tickets


# returns ( valid: bool, total of invalid values: int )
# (both are necessary because the invalid values might be 0's)
def validate(ticket, rules):
    err = 0
    valid = True
    for v in ticket:
        rules_fit = 0
        for cr in rules.values():
            if cr[0][0] <= v <= cr[0][1] or cr[1][0] <= v <= cr[1][1]:
                rules_fit += 1
        if rules_fit == 0:
            valid = False
            err += v
    return (valid, err)


# for a given ticket, return a list, each element of which is the list of
# fields whose rules that ticket element satisfies
def possible_fields(ticket, rules):
    fields = []
    for v in ticket:
        value_fields = []
        for fn, cr in rules.items():
            if cr[0][0] <= v <= cr[0][1] or cr[1][0] <= v <= cr[1][1]:
                value_fields.append(fn)
        fields.append(value_fields)
    return fields


# given a list of the lists-of-lists returned by possible_fields(), merge them
# all into a single list of lists of possible fields by intersecting the
# set of field names in each position
#
# in other words, this takes the list of lists of possible fields for each
# ticket element across a number of tickets, and merges them into a single
# list of lists of possible fields
def merge_possible(possible):
    s = [set(f) for f in possible[0]]
    for p in possible[1:]:
        s = [set(x).intersection(f) for x, f in zip(p, s)]
    return [list(x) for x in s]


# nondestructive remove()
def removed(x, a):
    return [e for e in a if e != x]


# figure out the assignment of field names to indices by repeatedly assigning
# the indices for which there is only one possible field name, and then
# removing that field name from all the other indices' possible-fields lists
#
# it is definitely possible to do this more cleanly and efficiently, but no
# need today
def solve_assignment(possible):
    d = {}
    while True:
        progress = False
        for i, p in enumerate(possible):
            if len(p) == 1:
                d[p[0]] = i
                progress = True
        if not progress:
            assert not any(possible)   # make sure we have a complete solution
            return d
        for f in d.keys():
            possible = [removed(f, a) for a in possible]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        sections = f.read().split("\n\n")

    rules = parse_rules(sections[0])
    mine = parse_tickets(sections[1])[0]
    nearby = parse_tickets(sections[2])

    # part 1
    print("Part 1:", sum([validate(t, rules)[1] for t in nearby]))

    # part 2
    assert validate(mine, rules)[0]
    nearby = [t for t in nearby if validate(t, rules)[0]]   # remove invalid
    pf = [possible_fields(f, rules) for f in [mine] + nearby]
    mpf = merge_possible(pf)
    asgn = solve_assignment(mpf)
    p = math.prod([mine[v]
                   for k, v in asgn.items() if k.startswith("departure")])
    print("Part 2:", p)
