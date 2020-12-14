import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        mem = {}
        for line in f:
            t = [x.strip() for x in line.split("=")]
            if t[0] == "mask":
                mask_str = line.split("=")[1].strip()
                ormask_str = mask_str.replace("X", "0")
                ormask = int(ormask_str, 2)
                andmask_str = mask_str.replace("X", "1")
                andmask = int(andmask_str, 2)
            else:
                assert t[0].startswith("mem")
                addr = int(t[0][4:-1])
                opd = (int(t[1]) & andmask) | ormask
                mem[addr] = opd

        print(sum(mem.values()))
