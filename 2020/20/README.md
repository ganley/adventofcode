# Day 20

[Puzzle](https://adventofcode.com/2020/day/20)

This was a fiddly one. Luckily this is [not the first time](http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=1&f=G&l=50&co1=AND&d=PTXT&s1=6161078.PN.&OS=PN/6161078&RS=PN/6161078)
I've worked with rotations and orientations.

I was nicely able to build off of the Grid class I wrote for Day 11.

I did a fairly obvious exhaustive search, relying on the fact that not many
tiles will fit. It runs plenty fast enough, it turns out. I feel like there
are many improvements possible. The elegant solution I considered but didn't
write was to build a graph whose vertices are oriented tiles and that has
edges between compatible tiles, and then find a grid subgraph. (It's a bit
trickier than that due to having to not use the same tile twice, and due to
both vertical and horizontal compatibility, but anyway.) Even aside from such
fancy business, my solution does a *lot* of unnecessary copying, most of which
could be eliminated with a little work.

sample.txt -> aoc20.py -> 20899048083289 (part 1) and 273 (part 2)

input.txt -> aoc20.py -> 47213728755493 (part 1) and 1599 (part 2)

Later, a coworker pointed out a property that was given that I missed, and
that could be used to make the solution more efficient: The sides that face
the outside won't match any other tile. I was actually lucky to miss this,
because it lures you into an easy solution for part 1 (the corners are the
only tiles with two edges that don't match any others) that doesn't help you
at all in part 2.
