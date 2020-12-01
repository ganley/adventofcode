import itertools
import sys

with open(sys.argv[1], "r") as f:
    nums = [ int(i) for i in f.read().split() ]

for a,b in itertools.combinations(nums, 2):
    if a + b == 2020:
        print("%d + %d = 2020" % ( a, b ) )
        print("%d * %d = %d" % ( a, b, a * b ) )

