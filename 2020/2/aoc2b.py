import sys

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

valid = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        occ, char, pwd = line.strip().split()
        char = char.strip(":")
        ix = [int(x) for x in occ.split("-")]
        count = len([i for i in ix if pwd[i - 1] == char])
        if count == 1:
            valid += 1

print(valid)
