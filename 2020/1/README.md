# Day 1

[Puzzle](https://adventofcode.com/2020/day/1)

A beautiful solution I saw, from "ryanchants" on RLS:

```python
    print(math.prod({sum(xs): xs for xs in itertools.product(*[list(map(int, input_string.split("\n")))]*2)}.get(2020)))
```

Replace the `*2` with `*3` for the second part of the problem.
