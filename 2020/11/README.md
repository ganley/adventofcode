# Day 11

[Puzzle](https://adventofcode.com/2020/day/11)

Cellular automaton! When I first got into computers in my early teens, I was
*obsessed* with cellular automata. I learned assembly language because
Conway's Game of Life didn't run fast enough on my TRS-80 in BASIC.

You're given a grid of floor (`.`), empty seat (`L`), or occupied seat (`#`).

Part 1: Empty seat gets filled if there are no filled seats immediately
adjacent to it in the 8 compass directions. Filled seat becomes empty if it
has 4 or more filled neighbors. How many filled seats when it stabilizes?

Part 2: Now neighbors aren't immediately adjacent, but the nearest seat you
can see along each of the 8 compass directions. And a filled seat becomes
empty if it has 5 or more filled neighbors now. Again, how many filled seats
when it stabilizes?

This code isn't as pythonic as I'd like, but I'm not going to take the time
to tighten it up right now (or possibly ever).

small.txt -> aoc2020\_11.py or aoc2020\_11.py -> 5 (both parts)

sample.txt -> aoc2020\_11.py -> 37 (part 1) and 26 (part 2)

input.txt -> aoc2020\_11.py -> 2359 (part 1) and 2131 (part 2)

