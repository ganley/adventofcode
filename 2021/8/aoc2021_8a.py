# quick and dirty part 1 solution, because I can guess what's coming
# and suspect that this won't be useful for part 2 at all

import sys


digits_by_num_segments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        total = 0
        for rawline in f:
            if line := rawline.strip():
                _, b = line.split('|')
                output = b.split()
                for d in output:
                    if len(d) in digits_by_num_segments:
                        total += 1

    print(total)
