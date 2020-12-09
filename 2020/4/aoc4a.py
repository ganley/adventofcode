import sys


required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def check(fields):
    return 1 if fields.issuperset(required) else 0


with open(sys.argv[1], "r") as f:
    valid = 0
    fields = set()
    for line in f:
        if vals := line.strip().split():
            for k, _ in [v.split(":") for v in vals]:
                fields.add(k)
        else:    # blank line
            valid += check(fields)
            fields.clear()
    valid += check(fields)      # last record may have no blank line after


print(valid)
