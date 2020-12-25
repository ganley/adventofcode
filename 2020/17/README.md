# Day 17

[Puzzle](https://adventofcode.com/2020/day/17)

Started from my code for Day 11. All I had to do was add a dimension and then
add another dimension, and of course adjust the generation rules.

sample.txt -> aoc17a.py -> 112

input.txt -> aoc17a.py -> 289

sample.txt -> aoc17b.py -> 848

input.txt -> aoc17b.py -> 2084

Enumerating over the entire NxNxN(xN) cube isn't the most efficient possible
implementation, but it'll do. Considering the region grows by 1 each
generation, and that I don't store empty cells at all, to do more efficiently
would be a bit complicated.
