import itertools
import sys


digits = {
    #    a      b      c     d       e      f      g
    (  True,  True,  True, False,  True,  True,  True ): 0,
    ( False, False,  True, False, False,  True, False ): 1,
    (  True, False,  True,  True,  True, False,  True ): 2,
    (  True, False,  True,  True, False,  True,  True ): 3,
    ( False,  True,  True,  True, False,  True, False ): 4,
    (  True,  True, False,  True, False,  True,  True ): 5,
    (  True,  True, False,  True,  True,  True,  True ): 6,
    (  True, False,  True, False, False,  True, False ): 7,
    (  True,  True,  True,  True,  True,  True,  True ): 8,
    (  True,  True,  True,  True, False,  True,  True ): 9
}


# builds the truth vector for a given display string and permutation
def vec(disp, perm):
    s = [ False ] * 7
    for c in disp:
        s[perm[ord(c) - ord('a')]] = True
    return tuple(s)


# enumerate all permutations and when one is found that is consistent
# with all of the output strings, use it to decode the output digits and
# return the resulting output number
def decode(displays, output):
    for p in itertools.permutations(range(7)):
        for d in displays:
            if not vec(d, p) in digits:
                break
        else:
            break
    else:
        assert false     # no permutation worked; shouldn't happen

    # when we get here, p is a permutation that works
    decoded = [str(digits[vec(o, p)]) for o in output]
    return int(''.join(decoded))
        

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        total = 0
        for rawline in f:
            if line := rawline.strip():
                left, right = line.split('|')
                displays = left.split()
                output = right.split()
                total += decode(displays, output)

    print(total)

