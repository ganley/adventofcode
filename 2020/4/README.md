# Day 4

[Puzzle](https://adventofcode.com/2020/day/4)

sample1.txt -> aoc2020\_4a.py -> 2

input.txt -> aoc2020\_4a.py -> 200

sample1.txt -> aoc2020\_4b.py -> still 2 (not useful)

sample2.txt -> aoc2020\_4b.py -> 4 (first 4 invalid, last 4 valid)

input.txt -> aoc2020\_4b.py -> 116

I realized later that even `hgt` can be done as a (only slightly ugly) regex,
but I'm going to leave it this way.

Also, an AoC lesson today: I added the special handling for the final record
that may not be followed by a newline, but many people I've talked to just
added a newline to the end of the input file instead. Given that I'm not a
contender anyway (due to not doing them at midnight), I feel okay about doing
it the "right" way.
