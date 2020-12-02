import itertools
import sys

with open(sys.argv[1], "r") as f:
    nums = [ int(i) for i in f.read().split() ]

for a,b,c in itertools.combinations(nums, 3):
    if a + b + c == 2020:
        print("{a} + {b} + {c} = 2020".format(a=a, b=b, c=c))
        print("{a} * {b} * {c} = {prod}".format(a=a, b=b, c=c, prod=a * b * c ))

