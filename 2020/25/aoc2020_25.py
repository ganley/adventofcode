import sys


def fn(n, s):
    return (n * s) % 20201227


def transform(num, iters):
    n = 1
    for i in range(iters):
        n = fn(n, num)
    return n


def loop_size(num, target):
    i = 0
    n = 1
    while n != target:
        n = fn(n, num)
        i += 1
    return(i)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        card, door = [int(x) for x in f.read().split()]

    card_loop = loop_size(7, card)
    door_loop = loop_size(7, door)

    card_privkey = transform(door, card_loop)
    door_privkey = transform(card, door_loop)

    assert card_privkey == door_privkey

    print(card_privkey)
