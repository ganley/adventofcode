import sys



grid = {}


def process_line(x0, y0, x1, y1):
    global grid

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            grid[(x0, y)] = grid.get((x0, y), 0) + 1

    elif y0 == y1:
        for x in range(x0, x1 + 1):
            grid[(x, y0)] = grid.get((x, y0), 0) + 1

    else: # diagonal
        # part 1 includes only horizontal and vertical lines
        # remove this 'return' for part 2
        #return

        for d in range(x1 - x0 + 1):
            x = x0 + d
            if y0 < y1:
                y = y0 + d
            else:
                y = y0 - d
            grid[(x, y)] = grid.get((x, y), 0) + 1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                pts = line.split(' -> ')
                x0, y0 = pts[0].split(',')
                x1, y1 = pts[1].split(',')
                process_line(int(x0), int(y0), int(x1), int(y1))

print(len([c for c in grid.values() if c > 1]))
