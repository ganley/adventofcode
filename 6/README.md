# Day 6

sample.txt -> aoc6a.py -> 11

input.txt -> aoc6a.py -> 6911

sample.txt -> aoc6b.py -> 6

input.txt -> aoc6b.py -> 3473

`for line in f:` is probably the right idiom for reading lines from a
file, since it's the only way I know of that doesn't read the whole file into
memory at once, but it annoys me to have to do `line.strip()` everywhere.
