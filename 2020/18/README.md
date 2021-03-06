# Day 18

[Puzzle](https://adventofcode.com/2020/day/18)

Parsing mathematical expressions!

When I learned compilers, I was taught that the
"[railroad](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)" algorithm
was the best way to parse math expressions, and it worked great here.
Hat tip to Professor J. A. N. Lee, who first taught me about this back in the
late 1980's.

Part 1: Evaluate an expression with (single-digit, it turns out, and I rely
on that) numbers, `+`, and `*`, and parentheses, but `+` and `*` have equal
precedence.

Part 2: Same, but now `+`, and `*` have the reverse of the usual precedence,
i.e. `+` is higher.

The code for part 1 and part 2 are both in `aoc2020_18.py`, with part 1
commented out. (They're both just calls to the same machinery with different
sets of precedences.)

sample1.txt -> 71 (part 1) and 231 (part 2)

sample2.txt -> 51 (both parts)

input.txt -> 12956356593940 (part 1) and 94240043727614 (part 2)

A coworker made a Python class that redefined `__add__` and `__mul__` to do
each other's operations, and then swapped those operators in the input and
evaluated.
