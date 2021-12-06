import sys



if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        for rawline in f:
            if line := rawline.strip():
                t = [int(x) for x in line.strip().split(',')]
                a = [len([y for y in t if y == x]) for x in range(9)]
                break

    #days = 80   # part 1
    days = 256  # part 2

    for d in range(days):
        a = a[1:7] + [a[7] + a[0]] + [a[8]] + [a[0]]

    print(sum(a))
