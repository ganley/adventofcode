import re
import sys



regexs = {
    "byr": "(19[2-9]\d|200[0-2])$",
    "iyr": "(201\d|2020)$",
    "eyr": "(202\d|2030)$",
    "hgt": "\d+(cm|in)$",
    "hcl": "\#[\dA-Fa-f]{6}$",
    "ecl": "(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": "\d{9}$"
}



def check(fields):
    for k,r in regexs.items():
        if not (k in fields and re.match(r, fields[k])):
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

    return 1



with open(sys.argv[1], "r") as f:
    valid = 0
    fields = {}
    for line in f:
        if vals := line.strip().split():
            for k,val in [ v.split(":") for v in vals ]:
                fields[k] = val
        else:    # blank line
            valid += check(fields)
            fields.clear()
    valid += check(fields)     # last record may have no blank line after



print(valid)

