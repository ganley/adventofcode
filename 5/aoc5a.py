import sys



def tr(string, fromchars, tochars):
    return ''.join([ tochars[fromchars.index(c)] for c in string ])



with open(sys.argv[1], "r") as f:
    seatids = [ int(tr(line.strip(), "FBLR", "0101"), 2) for line in f ]
    print(max(seatids))







