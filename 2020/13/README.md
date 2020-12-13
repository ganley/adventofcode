# Day 13

Fun with number theory.

Given: A start time and a set of intervals. Each interval *n* is either "x" or
else it indicates a bus that runs every  *n* minutes.

Part 1: Find the first time >= the start time that is served by any bus.

Part 2: Find the first time *t* such that time *t* is served by the first bus,
time *t* + 1 is served by the second bus, etc. The "x" entries are ignored but
count in the indexing; for example, if the input was "1,x,5", then you'd be
looking for a time such that time *t* is served by bus 1 and time *t* + 2 is
served by bus 5.

This is too big to do the obvious way, by just trying numbers. Probably too big
to sieve too. Fortunately there's a nice result called the [Chinese Remainder
Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
that tells us how to compute a number *x* such that *x* mod *aᵢ* = *nᵢ*
for all *i*. The key observations that allow us to apply the CRT are that
first, the inputs are all prime (they all have to be relatively prime to each
other in order for the CRT to work), and second, we're looking for an *x* such
that *x* mod *a₁* = 0, *x* + 1 mod *a₂* = 0, etc. The crucial insight
is that *x* + *k* mod *a* = 0 implies that *x* mod *a* = *a* - *k*. That
observation gives us the coefficients to plug into the CRT.

I grabbed the CRT code from
[Rosetta Code](https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6),
though I believe I fully understand it now and could reproduce it if I had to.

sample.txt -> aoc13a.py -> 295

input.txt -> aoc13a.py -> 4207

sample.txt -> aoc13b.py -> 1068781

input.txt -> aoc13b.py -> 725850285300475

(See what I mean about it being too big to search for?)
