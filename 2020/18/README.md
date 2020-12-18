# Day 18

Parsing mathematical expressions!

When I learned compilers, I was taught that the
"[railroad](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)" algorithm
was the best way to parse math expressions, and it worked great here.

Part 1: Evaluate an expression with (single-digit, it turns out, and I rely
on that) numbers, `+`, and `\*`, and parentheses, but `+` and `\*` have equal
precedence.

Part 2: Same, but now `+`, and `\*` have the reverse of the usual precedence,
i.e. `+` is higher.

The code for part 1 and part 2 are both in aoc18.py, with part 1 commented
out. (They're both just calls to the same machinery with different sets of
precedences.)

sample1.txt -> 71 (part 1) and 231 (part 2)

sample2.txt -> 51 (both parts)

input.txt -> 12956356593940 (part 1) and 94240043727614 (part 2)
