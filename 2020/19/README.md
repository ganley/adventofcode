# Day 19

You are given a bunch of text-matching rules, and then a bunch of strings to
validate against those rules. We are told that there are no loops in the rule
set. My strategy is to convert the rules into a regular expression and then
match against that.

For part 2, we are to replace two rules (the ones that make up the root rule)
with rules that *do* have loops in them. The trick here is to look at the
modified rules and see that they boil down to a root rule of
`(rule42)+(rule31)+`, with the additional constraint that there must be more
occurrences of rule42 than of rule31. A regular expression can't check that,
so we manually match the first half, then the second half, then check whether
the count constraint is satisfied.

sample.txt -> aoc19.py -> 2 (part 1) and error (part 2 N/A)

input.txt -> aoc19.py -> 200 (part 1) and 407 (part 2)

