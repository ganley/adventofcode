import copy
import functools
import itertools
import re
import string
import sys


# returns ( accumulator value, final value of pc )
def run(mem):
    pc = 0
    acc = 0
    visited = set()
    while not pc in visited and 0 <= pc < len(mem):
        visited.add(pc)

        if mem[pc][0] == "acc":
            acc += int(mem[pc][1])
            pc += 1
        elif mem[pc][0] == "jmp":
            pc += int(mem[pc][1])
        elif mem[pc][0] == "nop":
            pc += 1

    return (acc, pc)


def mutate(mem):
    for i in range(len(mem)):
        newmem = copy.deepcopy(mem)
        if mem[i][0] == "jmp":
            newmem[i][0] = "nop"
            acc, pc = run(newmem)
            if pc == len(mem):
                return (acc, pc)
        elif mem[i][0] == "nop":
            newmem[i][0] = "jmp"
            acc, pc = run(newmem)
            if pc == len(mem):
                return (acc, pc)

    return None


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        mem = [instr.split() for instr in f.readlines()]

    # part 1
    print(run(mem)[0])

    # part 2
    print(mutate(mem)[0])
