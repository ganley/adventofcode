import sys


# (x,y,wx,wy)
def sail(instrs):
    x, y = 0, 0
    wx, wy = 10, 1      # waypoint
    for ins in instrs:
        op = ins[0]
        val = int(ins[1:])
        if op == "N":
            wy += val
        elif op == "S":
            wy -= val
        elif op == "E":
            wx += val
        elif op == "W":
            wx -= val
        elif op == "L":
            assert val % 90 == 0
            while val > 0:
                wx, wy = -wy, wx
                val -= 90
        elif op == "R":
            assert val % 90 == 0
            while val > 0:
                wx, wy = wy, -wx
                val -= 90
        elif op == "F":
            x += wx * val
            y += wy * val
        else:
            assert False
    return (x, y, wx, wy)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        instrs = [line.strip() for line in f]

    x, y, _, _ = sail(instrs)

    print(abs(x) + abs(y))
