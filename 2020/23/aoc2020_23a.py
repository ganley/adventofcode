
# invariant: ring is rotated so that it always begins with the current cup
def go(txt, num_moves):
    ring = [int(x) for x in list(txt)]
    low = min(ring)
    high = max(ring)
    for m in range(num_moves):
        pull = ring[1:4]           # next three
        ring = [ring[0]] + ring[4:]
        dest = ring[0] - 1 if ring[0] > low else high
        while dest in pull:
            dest -= 1
            if dest < low:
                dest = high
        dest_ix = ring.index(dest)
        ring = ring[:(dest_ix + 1)] + pull + ring[(dest_ix + 1):]
        ring = ring[1:] + [ring[0]]
    return ring


if __name__ == "__main__":
    num_moves = 100
    # txt = "389125467"       # sample
    txt = "123487596"       # input

    order = go(txt, num_moves)

    ix1 = order.index(1)
    print("".join([str(x) for x in order[(ix1 + 1):] + order[:ix1]]))
