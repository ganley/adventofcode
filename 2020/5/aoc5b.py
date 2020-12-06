import sys


def tr(string, fromchars, tochars):
    return ''.join([tochars[fromchars.index(c)] for c in string])


with open(sys.argv[1], "r") as f:
    seatids = set([int(tr(line.strip(), "FBLR", "0101"), 2) for line in f])

    for i in range(1, 1023):
        if not i in seatids and (i - 1) in seatids and (i + 1) in seatids:
            print(i)
