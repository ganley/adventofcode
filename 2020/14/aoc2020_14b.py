import copy
import sys


def set(mem, addr, mask, val):
    xmap = [i for i in range(36) if mask[i] == "X"]
    bits = len(xmap)
    addr_chars = list("{:036b}".format(addr))
    # set the 1 bits
    for i, c in enumerate(mask):
        if c == "1":
            addr_chars[i] = "1"
    # do all possible values of the X bits
    for x in range(1 << bits):
        modaddr_chars = copy.copy(addr_chars)
        fmt = "{:0" + str(len(xmap)) + "b}"
        binary = fmt.format(x)
        for i, c in enumerate(binary):
            modaddr_chars[xmap[i]] = c
        modaddr = int(''.join(modaddr_chars), 2)     # not actually necessary
        mem[modaddr] = val


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        mem = {}
        for line in f:
            t = [x.strip() for x in line.split("=")]
            if t[0] == "mask":
                mask = line.split("=")[1].strip()
            else:
                assert t[0].startswith("mem")
                addr = int(t[0][4:-1])
                opd = int(t[1])
                set(mem, addr, mask, opd)

        print(sum(mem.values()))
