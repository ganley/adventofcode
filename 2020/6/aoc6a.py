import sys

with open(sys.argv[1], "r") as f:
    total = 0
    questions = set()
    for rawline in f:
        if line := rawline.strip():
            questions.update([c for c in line])
        else:   # blank line
            total += len(questions)
            questions.clear()

    total += len(questions)    # in case no final blank line

    print(total)
