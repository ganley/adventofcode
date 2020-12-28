import string
import sys

with open(sys.argv[1], "r") as f:
    total = 0
    questions = set(list(string.ascii_lowercase))
    for rawline in f:
        if line := rawline.strip():
            qs = set([c for c in line])
            questions = questions.intersection(qs)
        else:   # blank line
            total += len(questions)
            questions = set(list(string.ascii_lowercase))

    total += len(questions)    # in case no final blank line

    print(total)
