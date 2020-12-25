# Day 23

[Puzzle](https://adventofcode.com/2020/day/23)

Play a game: You have a ring of cups labeled 1 through 9 (not in order).
At each turn, take the 3 cups clockwise of the current cup. Choose a
destination cup that is the first cup whose label is less than the current
cup's but that isn't in the set of 3 you're removing. (If you go below 1,
you wrap around to the maximum label.) Reinsert the 3 cups, in their original
order, after the destination cup.

Part 1: Do this 100 times, and report the resulting order, clockwise from
(and not including) the cup labeled "1".

Part 2: Now, in addition to the given 9 cups, you have another 999,991 cups
labeled from 10 through 1000000, in that order. Play the same game, but now
for 10,000,000 turns. Report the product of the labels on the two cups that
are clockwise of the cup labeled "1" when you're done.

For the first time this AoC, I had to throw away my part 1 code and write
part 2 from scratch in a different language. The Python version performed only
83K moves in the ~45 minutes that I was rewriting it in C++. (Sequential
search -- the `index` function -- to find the index of an element in a
million-element list is very slow.)

I suspect that it might be possible to do essentially what I did in C++ in
Python, but I wasn't sufficiently confident that would be fast enough to go
that route.

For both parts, the sample and input values are hardwired in the code; you
have to uncommment the one you want.

aoc23a.py with sample input -> 67384529

aoc23a.py with real input -> 47598263

Compile aoc23b.cpp in the obvious way.

aoc23b.cpp with sample input -> 149245887792

aoc23b.cpp with real input -> 248009574232

I later realized I could have stuck with Python and just used a dictionary
mapping label to next label. Oh well.
