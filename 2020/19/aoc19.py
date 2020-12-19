import re
import sys


def parse_rules(txt):
    rules = {}
    for line in txt.split("\n"):
        rule_num, rule_txt = line.split(": ")
        if rule_txt.startswith("\""):
            rules[int(rule_num)] = rule_txt.replace("\"", "")
        else:
            parts = rule_txt.split(" | ")
            rules[int(rule_num)] = [[int(x) for x in p.split()] for p in parts]
    return rules


def regex(rule_num, rules):
    rule = rules[rule_num]
    if isinstance(rule, str):
        return rule
    else:
        clauses = ["".join([regex(p, rules) for p in parts]) for parts in rule]
        return "(" + "|".join(clauses) + ")"


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        rule_sect, msg_sect = f.read().split("\n\n")

    rules = parse_rules(rule_sect)
    msgs = [line.strip() for line in msg_sect.split()]

    # part 1
    rex = re.compile(regex(0, rules) + "$")
    print("Part 1:", len([m for m in msgs if rex.match(m)]))

    # part 2
    rex_front = re.compile(f"{regex(42, rules)}+")
    rex_back = re.compile(f"({regex(31, rules)})+$")

    c = 0
    for m in msgs:
        if match_front := rex_front.match(m):
            txt = match_front.group(0)
            rest = m[len(txt):]
            if match_back := rex_back.match(rest):
                if len(match_back.group(0)) < len(txt):
                    c += 1
    print("Part 2:", c)
