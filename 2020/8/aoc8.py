import copy
import sys


# returns ( accumulator value, final value of pc )
def run(mem):
    pc = 0
    acc = 0
    visited = set()
    while not pc in visited and 0 <= pc < len(mem):
        visited.add(pc)

        acc, pc = {
            "acc": (acc + mem[pc][1], pc + 1),
            "jmp": (acc, pc + mem[pc][1]),
            "nop": (acc, pc + 1)
        }[mem[pc][0]]

    return (acc, pc)


def mutate(mem):
    for i in range(len(mem)):
        if mem[i][0] == "jmp":
            mem[i][0] = "nop"
            acc, pc = run(mem)
            mem[i][0] = "jmp"   # restore
            if pc == len(mem):
                return (acc, pc)
        elif mem[i][0] == "nop":
            mem[i][0] = "jmp"
            acc, pc = run(mem)
            mem[i][0] = "nop"   # restore
            if pc == len(mem):
                return (acc, pc)

    return None


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        mem = [[ins, int(opd)] for ins, opd in
               [instr.split() for instr in f.readlines()]]

    # part 1
    print(run(mem)[0])

    # part 2
    print(mutate(mem)[0])
