# Day 16

[Puzzle](https://adventofcode.com/2020/day/16)

We're given rules for each field name, each of which is a pair of allowable
numerical ranges, and then a bunch of tickets, each of which is a list of
integers.

Part 1: Find the total of all the values in the tickets that are invalid, i.e.
are not within the allowable ranges for any field.

Part 2: After discarding the invalid tickets, find a valid assignment of fields
to ticket value indices. Having done so, emit the product of the field values
in your own ticket for every field that starts with "departure".

This one gave me the most trouble so far this year. It turns out there are
tickets whose only invalid values are 0's, so if you're checking for validity
by whether the sum of invalid values is positive (as I was) you're going to
let through some invalid tickets, which is going to leave no solution for
part 2. That cost me at least half an hour.

sample.txt -> aoc2020\_16.py -> 71 (part 1) - part 2 N/A

input.txt -> aoc2020\_16.py -> 30869 (part 1) and 4381476149273 (part 2)

This code is not as polished as it could be; some things are done procedurally
that could be rewritten functionally, and some things are done less efficiently
than they could be. However, I spent as much time on today as I want to.
