import sys


def fold(pts, axis, value):
    new = set()
    for p in list(pts):
        if axis == 'x':
            if p[0] >= value:
                new.add((2 * value - p[0], p[1]))
            else:
                new.add((p[0], p[1]))
        else:
            assert axis == 'y'
            if p[1] >= value:
                new.add((p[0], 2 * value - p[1]))
            else:
                new.add((p[0], p[1]))
    return new


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        pts = set()
        for rawline in f:
            if line := rawline.strip():
                if line.startswith('fold'):
                    t = line.split()
                    assert t[0] == 'fold' and t[1] == 'along'
                    axis, value = t[2].split('=')
                    value = int(value)
                    pts = fold(pts, axis, value)
                    print(len(pts))   # part 1: first of these
                else:
                    t = line.split(',')
                    pts.add((int(t[0]), int(t[1])))

    # part 2: the letters in this image
    mx = max([p[0] for p in pts]) + 1
    my = max([p[1] for p in pts]) + 1
    s = [['.'] * mx for _ in range(my)]
    for x, y in list(pts):
        s[y][x] = '#'
    for row in s:
        print(''.join(row))

