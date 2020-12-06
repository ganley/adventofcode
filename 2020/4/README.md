# Day 4

aoc4a.py -> sample1.txt -> 2

aoc4a.py -> input.txt -> 200

aoc4b.py -> sample1.txt -> still 2 (not useful)

aoc4b.py -> sample2.txt -> 4 (first 4 invalid, last 4 valid)

aoc4b.py -> input.txt -> 116

I realized later that even `hgt` can be done as a (only slightly ugly) regex,
but I'm going to leave it this way.

Also, an AoC lesson today: I added the special handling for the final record
that may not be followed by a newline, but many people I've talked to just
added a newline to the end of the input file instead. Given that I'm not a
contender anyway (due to not doing them at midnight), I feel okay about doing
it the "right" way.
