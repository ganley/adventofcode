import sys

required = set([ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ])

def check(fields):
    if fields.issuperset(required):
        return 1
    else:
        return 0

with open(sys.argv[1], "r") as f:
    valid = 0
    fields = set()
    for line in f:
        vals = line.strip().split()
        if vals:
            for k,_ in [ v.split(":") for v in vals ]:
                fields.add(k)
        else:    # blank line
            valid += check(fields)
            fields.clear()
    valid += check(fields)      # last record may have no blank line after

print(valid)

