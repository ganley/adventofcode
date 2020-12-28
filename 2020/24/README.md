# Day 24

[Puzzle](https://adventofcode.com/2020/day/24)

Hexagonal cellular automaton!

Part 1: We are given coordinates of tiles in a hexagonal grid to flip (white
to black or black to white; they start all white). Coordinates are an
undelimited sequence of ordinal directions from `e`, `w`, `ne`, `nw`, `se`,
and `sw`. Report how many black tiles after doing the flipping.

Part 2: Cellular automaton starting with the configuration from part 1.
Black tiles become white if they have 0 or more than 2 black neighbors, white
tiles become back if they have exactly 2 black neighbors. Report the number
of black tiles after 100 iterations.

Once again I got to reuse my code from Day 11.

aoc2020\_24.py -> sample.txt -> 10 (part 1) and 2208 (part 2)

aoc2020\_24.py -> input.txt -> 339 (part 1) and 3794 (part 2)
