import math
import sys

from tile import Tile


# return the given tile, oriented in one of the 8 orientations
def orient(tile, ornum):
    assert 0 <= ornum <= 7
    t = tile
    if ornum & 1:
        t = t.flipx()
    if ornum & 2:
        t = t.flipy()
    if ornum & 4:
        t = t.rotate()
    return t


# find a size x size arrangement that fits together
# partial is a list of Tiles
# tiles is a dictionary of id:Tile
def search(partial, size, tiles):
    done = [p.id for p in partial]

    nextix = len(partial)
    if nextix == len(tiles):     # all filled in
        return partial

    col = nextix % size
    row = nextix // size
    for id in tiles.keys():
        if id not in done:    # not already placed
            for ornum in range(8):
                placed = orient(tiles[id], ornum)
                if (col == 0 or partial[nextix - 1].matches_right(placed)) and \
                   (row == 0 or partial[nextix - size].matches_down(placed)):
                    partial.append(placed)
                    if p := search(partial, size, tiles):
                        return p
                    else:
                        partial.pop(-1)
    return None


# build the big image out of the placed sub-images
#
# assumptions:
#   len(solution) is a perfect square
#   every tile is the same size
#   every tile is square
def build_image(solution):
    size = int(math.sqrt(len(solution)))
    w = solution[0].width - 2
    h = solution[0].height - 2
    assert w == h
    image = Tile()
    image.id = 0
    image.width = w * size
    image.height = h * size
    for i, t in enumerate(solution):
        col = i % size
        row = i // size
        for coord in t.grid.keys():
            x = coord[0] - 1
            y = coord[1] - 1
            if x >= 0 and y >= 0 and x < w and y < h:    # skip the edges
                image.set(col * w + x, row * h + y, "#")
    return image


# read the monster image into a Tile
def monster():
    m = Tile()
    with open("monster.txt", "r") as f:
        m.read(f, ".")
    return m


# find all matches to the given monster image and mark them with O's
def find_and_mark(image, monster):
    for x in range(image.width - monster.width + 1):
        for y in range(image.height - monster.height + 1):
            for coord in monster.grid.keys():
                if not image.get(coord[0] + x, coord[1] + y):
                    break
            else:    # found one
                for coord in monster.grid.keys():
                    image.set(coord[0] + x, coord[1] + y, "O")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        tiles_txt = f.read().split("\n\n")

    tiles = [Tile(t.split("\n"), ".") for t in tiles_txt]
    tile_dict = {t.id: t for t in tiles}

    # find a valid placement of tiles
    size = int(math.sqrt(len(tiles)))
    s = search([], size, tile_dict)
    print("Part 1:",
          s[0].id * s[size - 1].id * s[len(tiles) - 1].id * s[len(tiles) - size].id)

    # build the big image
    img = build_image(s)

    # read the monster, and mark it in all orientations
    m = monster()
    for ornum in range(8):
        find_and_mark(img, orient(m, ornum))

    # count the remaining "rough seas" ("#" not covered by a monster)
    c = 0
    for coord in img.grid.keys():
        if img.get(coord[0], coord[1]) == "#":
            c += 1

    print("Part 2:", c)
