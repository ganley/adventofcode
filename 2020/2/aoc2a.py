import sys

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

valid = 0
with open (sys.argv[1], "r") as f:
    for line in f:
        occ,char,pwd = line.strip().split()
        char = char.strip(":")
        lo,hi = ( int(x) for x in occ.split("-") )
        count = len([ x for x in pwd if x == char ])
        if count >= lo and count <= hi:
            valid += 1
            
print(valid)
