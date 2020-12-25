# Day 6

[Puzzle](https://adventofcode.com/2020/day/6)

sample.txt -> aoc6a.py -> 11

input.txt -> aoc6a.py -> 6911

sample.txt -> aoc6b.py -> 6

input.txt -> aoc6b.py -> 3473

I realized afterward that part B would fail if there *was* a blank line at
the end of the file, as it would count that as a 26. I'm not going to bother
fixing it.

`for line in f:` is probably the right idiom for reading lines from a
file, since it's the only way I know of that doesn't read the whole file into
memory at once, but it annoys me to have to do `line.strip()` everywhere.
