import string
import sys


# this relies on the fact that only single digits are used
# if that weren't true we'd have to do a little more work here
def tokenize(expr):
    s = expr.replace(" ", "")
    return list(s)


# takes an expression (tokenized) and a dict mapping operators to precedence
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def parse(expr, prec):
    t = tokenize(expr)
    out = []
    ops = []
    for e in t:
        if e in string.digits:   # need more sophisticated check if >1 digit
            out.append(int(e))
        elif e in prec:
            while ops and ops[-1] in prec and prec[ops[-1]] >= prec[e]:
                out.append(ops.pop())
            ops.append(e)
        elif e == "(":
            ops.append(e)
        elif e == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            assert ops and ops[-1] == "("
            ops.pop()   # discard (
        else:
            assert False
    while ops:
        out.append(ops.pop())
    return out


def evaluate(stack):
    s = []
    for c in stack:
        if isinstance(c, int):
            s.append(c)
        elif c == "+":
            s.append(s.pop() + s.pop())
        elif c == "*":
            s.append(s.pop() * s.pop())
        else:
            assert False
    assert s and len(s) == 1 and isinstance(s[0], int)
    return s[0]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        total = 0
        for rawline in f:
            if line := rawline.strip():
                # part 1:
                #total += evaluate(parse(line, {"+" : 1, "*" : 1}))

                # part 2:
                total += evaluate(parse(line, {"+": 2, "*": 1}))
    print(total)
