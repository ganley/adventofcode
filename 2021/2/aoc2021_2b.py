import sys


if __name__ == "__main__":
    pos = 0
    aim = 0
    depth = 0
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                t = line.split()
                cmd, amt = t[0], int(t[1])
                pos, aim, depth = {
                    "forward": (pos + amt, aim, depth + aim * amt),
                    "down": (pos, aim + amt, depth),
                    "up": (pos, aim - amt, depth)
                }[cmd]

    print(f'{pos=} {depth=} product={pos*depth}')

