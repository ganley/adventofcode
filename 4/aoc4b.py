import re
import sys



regexs = {
    "byr": "^\d{4}$",
    "iyr": "^\d{4}$",
    "eyr": "^\d{4}$",
    "hgt": "^\d+(cm|in)$",
    "hcl": "^\#[\dA-Fa-f]{6}$",
    "ecl": "^[a-z]{3}$",
    "pid": "^\d{9}$"
}


def check(fields):
    for k,r in regexs.items():
        if not (k in fields and re.match(r, fields[k])):
            return 0

    if not 1920 <= int(fields["byr"]) <= 2002:
        return 0

    if not 2010 <= int(fields["iyr"]) <= 2020:
        return 0

    if not 2020 <= int(fields["eyr"]) <= 2030:
        return 0

    hgt = int(fields["hgt"][:-2])
    units = fields["hgt"][-2:]
    if units == "cm":
        if not 150 <= hgt <= 193:
            return 0
    elif units == "in":
        if not 59 <= hgt <= 76:
            return 0
    else:
        return 0

    if not fields["ecl"] in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]:
        return 0

    return 1



with open(sys.argv[1], "r") as f:
    valid = 0
    fields = {}
    for line in f:
        vals = line.strip().split()
        if vals:
            for k,val in [ v.split(":") for v in vals ]:
                fields[k] = val
        else:    # blank line
            valid += check(fields)
            fields.clear()
    valid += check(fields)     # last record may have no blank line after

print(valid)

