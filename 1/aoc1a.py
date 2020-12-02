import itertools
import sys

with open(sys.argv[1], "r") as f:
    nums = [ int(i) for i in f.read().split() ]

for a,b in itertools.combinations(nums, 2):
    if a + b == 2020:
        print("{a} + {b} = 2020".format(a=a, b=b))
        print("{a} * {b} = {prod}".format(a=a, b=b, prod=a * b))

