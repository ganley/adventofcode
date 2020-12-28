import copy
import sys


def combat(deck1, deck2):
    while deck1 and deck2:
        play1 = deck1.pop(0)
        play2 = deck2.pop(0)
        if play1 > play2:
            deck1 += [play1, play2]
        else:
            deck2 += [play2, play1]
    return (deck1, deck2)


def recursive_combat(deck1, deck2):
    played_states = set()
    while deck1 and deck2:
        state = tuple(deck1 + [-1] + deck2)
        if state in played_states:
            return (deck1, [])
        played_states.add(state)

        play1 = deck1.pop(0)
        play2 = deck2.pop(0)
        if len(deck1) >= play1 and len(deck2) >= play2:
            # recursive combat
            subdeck1 = copy.copy(deck1[:play1])
            subdeck2 = copy.copy(deck2[:play2])
            result1, result2 = recursive_combat(subdeck1, subdeck2)
            if result1:
                deck1 += [play1, play2]
            else:
                assert result2
                deck2 += [play2, play1]
        else:
            # regular play
            if play1 > play2:
                deck1 += [play1, play2]
            else:
                deck2 += [play2, play1]
    return (deck1, deck2)


def score(deck):
    return sum([m * c for c, m in enumerate(reversed(deck), start=1)])


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        parts = f.read().split("\n\n")
        deck1 = [int(x) for x in parts[0].split("\n")[1:] if x]
        deck2 = [int(x) for x in parts[1].split("\n")[1:] if x]

    # Part 1
    after1, after2 = combat(copy.copy(deck1), copy.copy(deck2))
    print("Part 1:", score(after1) if after1 else score(after2))

    # Part 2
    after1, after2 = recursive_combat(deck1, deck2)
    print("Part 2:", score(after1) if after1 else score(after2))
