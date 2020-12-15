# Day 15

Today's lesson: Read the problem carefully.

Given a starting sequence of numbers, "speak" subsequent numbers by this
algorithm:

 * If the last number spoken had just been spoken for the first time, say 0.
 * Otherwise, say the difference in sequence number between the previous time it
   was spoken and the time before that.

(This is the Van Eck sequence, or very similar to it.)

Part 1: What is the 2,020th number spoken?

Part 2: What is the 30,000,000th number spoken?

To my mild surprise, I was able to use the exact same code for Part 2 as for
Part 1.

sample1.txt -> aoc15.py -> 436 (part 1) and 175594 (part 2)

input.txt -> aoc15.py -> 260 (part 1) and 950 (part 2)
