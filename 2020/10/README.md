# Day 10

[Puzzle](https://adventofcode.com/2020/day/10)

You have a set of voltage adapters, each of which can work at a particular
number of "jolts", with a margin of up to 3 jolts. The set of adapters is
such that every adapter handles either 1 more or 3 more jolts than the next
smallest one.

Part 1: Figure out the number of adapters that handle 1 more than the next
smallest one and the number that handle 3 more, and produce the product of
those two numbers.

Part 2: Figure out how many distinct chains of your adapters you could use
such that there isn't a difference of 4 or more jolts anywhere along the
chain. There are enough that brute-force recursion is impractical.

The key insight for part 2 is that each "streak" of delta-1's is independent
of every other, since you can never remove a delta-3 adapter from the chain.
For every chain of delta-1's, you can't remove the last one (as that would
create a gap of 4 to the next one), but you can remove up to 2 of any of the
remaining ones. The answer is the product of the values of this expression for
every streak of delta-1's. The code might be clearer than that explanation.

sample1.txt -> aoc10.py -> 35 (part 1) and 8 (part 2)

sample2.txt -> aoc10.py -> 220 (part 1) and 19208 (part 2)

input.txt -> aoc10.py -> 2475 (part 1) and 442136281481216 (part 2)

Note: The problem specification stated that there could be adapters with a
gap of 2 from the next-lower one, but none appear in the input. Beware for
this to potentially appear in a future puzzle.
