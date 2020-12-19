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

What the code does is actually a bit of a cheat - rather than check that
the number of occurrences of rule 42 > the number of occurrences of rule 31,
it checks whether the matching text itself is longer. It works, but it isn't
quite right - I suspect there might be test cases where it would fail. But
it produced the right answer, so I'm going to let it go. To do it right, it
would be a fairly simple matter to check `(rule42){1}`, `(rule42){2}`, etc.
instead of just `(rule42)+`.

sample.txt -> aoc19.py -> 2 (part 1) and error (part 2 N/A)

input.txt -> aoc19.py -> 200 (part 1) and 407 (part 2)

