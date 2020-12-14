# Day 14

Binary manipulation. I made a classic AoC blunder: I did Part 1 using bitwise
operations, and that trapped me into that mindset, but Part 2 is better
done by keeping the string representations. The version you see here was
rewritten to do just that, but the original version was a real mess. Lots
of conversions between bit indices (which index from the right) and string
indices (which index from the left) provided lots of hiding places for bugs.

Part 1: You're given a bitmask and a series of memory assignments; for each
assignment, apply the bitmask to the operand such that 0's are overwritten
with 0, 1's are overwritten with 1, and X's are left alone. Print the total
of all the values in memory at the end.

Part 2: Now the bitmask applies to the address instead of the operand. It sets
any bit that is 1 in the mask to 1, leaves bits that are 0 in the mask alone,
and enumerates all possible values for the X bits in the mask, setting the
values of all of those addresses to the operand.

aoc14a.py -> sample1.txt -> 165

aoc14a.py -> input.txt -> 10717676595607

aoc14b.py -> sample2.txt -> 208

aoc14b.py -> input.txt -> 3974538275659
