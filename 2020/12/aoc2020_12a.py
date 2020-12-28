import math
import sys


# (x,y,theta)
def sail(instrs):
    x, y = 0.0, 0.0
    t = 0.0
    for ins in instrs:
        op = ins[0]
        val = float(ins[1:])
        x, y, t = {
            "N": (x, y + val, t),
            "S": (x, y - val, t),
            "E": (x + val, y, t),
            "W": (x - val, y, t),
            "L": (x, y, t + val),
            "R": (x, y, t - val),
            "F": (x + val * math.cos(math.radians(t)),
                  y + val * math.sin(math.radians(t)), t)
        }[op]
    return (x, y, t)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        instrs = [line.strip() for line in f]

    x, y, _ = sail(instrs)

    print(abs(x) + abs(y))
