import sys


match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


# returns (unexpected character or None on successful parse,
#          remaining stack)
def parse(s):
    stack = []
    for c in s:
        if c in match:
            stack.append(c)
        else:
            if c == match.get(stack[-1]):
                stack.pop()
            else:
                return (c, stack)    # unexpected char

    return (None, stack)


def compute_score(s):
    score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    total = 0
    for c in reversed(s):
        total = total * 5 + score[c]

    return total
    
        
if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        scores = []
        for rawline in f:
            if line := rawline.strip():
                badchar, stack = parse(line)
                if not badchar:
                    scores.append(compute_score(stack))

    print(sorted(scores)[len(scores) // 2])
