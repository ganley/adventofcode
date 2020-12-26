import copy
import functools
import itertools
import math
import re
import string
import sys


def path_to_segments(path):
    segs = []
    x, y = 0, 0
    for d in path.split(","):
        x0, y0 = x, y
        direction,magnitude = d[0], int(d[1:])
        dx, dy = {
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1),
            "L": (-1, 0)
        }[direction]
        x += dx * magnitude
        y += dy * magnitude
        segs.append(((x0, y0), (x, y)))
    return segs



def intersect(seg0, seg1):
    x00, y00, x01, y01 = seg0[0][0], seg0[0][1], seg0[1][0], seg0[1][1]
    x10, y10, x11, y11 = seg1[0][0], seg1[0][1], seg1[1][0], seg1[1][1]

    if x00 == x01:  # seg0 is vertical
        if x10 == x11:  # seg1 also vertical
            return None
        x10, x11 = min(x10, x11), max(x10, x11)
        y00, y01 = min(y00, y01), max(y00, y01)
        if x10 <= x00 <= x11 and y00 <= y10 <= y01:
            return (x01, y10)
        return None
    else:           # seg0 is horizontal
        x00, x01 = min(x00, x01), max(x00, x01)
        y10, y11 = min(y10, y11), max(y10, y11)
        if x00 <= x10 <= x01 and y10 <= y00 <= y11:
            return (x10, y00)
        return None


def max_coords(segs_list):
    if not segs_list:
        return None
    x, y = segs_list[0][0][0][0], segs_list[0][0][0][1]
    for segs in segs_list:
        for s in segs:
            x = max([x, s[0][0], s[1][0]])
            y = max([y, s[0][1], s[1][1]])
    return (x, y)


def l1dist(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def find_closest_intersection(segs0, segs1):
    x, y = max_coords([segs0, segs1])
    bestdist = l1dist((0, 0), (x, y))
    for s0 in segs0:
        for s1 in segs1:
            cross = intersect(s0, s1)
            if cross:
                dist = l1dist((0, 0), cross)
                if dist < bestdist and dist > 0:
                    bestdist = dist
                    x, y = cross
    return (x, y)


def find_mindelay_intersection(segs0, segs1):
    x, y = max_coords([segs0, segs1])
    bestdelay = sum([l1dist(s[0], s[1]) for s in segs0] + [l1dist(s[0], s[1]) for s in segs1])
    delay0 = 0
    for s0 in segs0:
        delay1 = 0
        for s1 in segs1:
            cross = intersect(s0, s1)
            if cross:
                delay = delay0 + delay1 + l1dist(s0[0], cross) + l1dist(s1[0], cross)
                if delay < bestdelay and delay > 0:
                    bestdelay = delay
                    x, y = cross
            delay1 += l1dist(s1[0], s1[1])
        delay0 += l1dist(s0[0], s0[1])
    return ((x, y), bestdelay)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        paths = [line.strip() for line in f]

    assert len(paths) == 2
    segs0 = path_to_segments(paths[0])
    segs1 = path_to_segments(paths[1])
    cross = find_closest_intersection(segs0, segs1)
    print("Part 1:", l1dist((0, 0), cross))

    _, delay = find_mindelay_intersection(segs0, segs1)
    print("Part 2:", delay)

