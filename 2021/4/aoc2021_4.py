import sys


def winner(b):
    for i in range(5):
        for j in range(5):
            if b[i][j] >= 0:
                break
        else:
            return True

    for j in range(5):
        for i in range(5):
            if b[i][j] >= 0:
                break
        else:
            return True


def score(b):
    s = 0
    for row in b:
        for x in row:
            if x >= 0:
                s += x
    return s


if __name__ == "__main__":
    calls = []
    boards = []
    with open(sys.argv[1], "r") as f:
        board = []
        for rawline in f:
            if line := rawline.strip():
                if not calls:
                    calls = [int(x) for x in line.split(',')]
                else:
                    row = [int(x) for x in line.split()]
                    if len(board) == 5:
                        boards.append(board)
                        board = [row]
                    else:
                        board.append(row)
        if board:
            assert len(board) == 5
            boards.append(board)

    #aocpart = 1
    aocpart = 2

    for c in calls:
        for b in boards:
            for i in range(5):
                for j in range(5):
                    if b[i][j] == c:
                        b[i][j] = -c - 1
        newboards = []
        for b in boards:
            if winner(b):
                if aocpart == 1 or len(boards) == 1:
                    print(f'score={score(b)} answer={score(b) * c}')
                    sys.exit(0)
            else:
                newboards.append(b)
        boards = newboards

