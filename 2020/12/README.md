# Day 12

[Puzzle](https://adventofcode.com/2020/day/12)

You have a ship with a position and heading, and are given a series of
instructions.

Part 1: NSEW move the given amount in that direction, LR rotate the ship by
the given number of degrees, F moves the ship forward the given amount.

Part 2: There is a waypoint relative to the ship. The instructions move the
waypoint, not the ship, except for F which moves the ship to the waypoint the
given number of times. (The waypoint is relative to the ship.)

A cautionary AoC tale: I started without looking at the input file, and assumed
that the R/L angles could have any value. Thus, I did things trigonometrically,
which worked for Part 1 but got me totally wound around the axle in Part 2.
Then I realized that the angles are all right angles, so no trig is required.
I then did Part 2 without trig (and also without the fancy dict dispatch I used
in Part 1). Let this be a lesson: Look at the inputs to verify any assumptions
you've made before you begin.

aoc12a.py -> sample.py -> 25

aoc12a.py -> input.py -> 796

aoc12b.py -> sample.py -> 286

aoc12b.py -> input.py -> 39446

