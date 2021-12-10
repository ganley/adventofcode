import sys


match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


# returns unexpected character, or None on successful parse
def parse(s):
    stack = []
    for c in s:
        if c in match:
            stack.append(c)
        else:
            if c == match.get(stack[-1]):
                stack.pop()
            else:
                return c    # unexpected char

    return None
     
        
if __name__ == "__main__":
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    with open(sys.argv[1], "r") as f:
        total = 0
        for rawline in f:
            if line := rawline.strip():
                c = parse(line)
                if c:
                    total += score[c]

    print(total)
