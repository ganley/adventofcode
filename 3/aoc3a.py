import sys

#    ..##.......
#    #...#...#..
#    .#....#..#.
#    ..#.#...#.#
#    .#...##..#.
#    ..#.##.....
#    .#.#.#....#
#    .#........#
#    #.##...#...
#    #...##....#
#    .#..#...#.#

def ReadGrid(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            row = line.strip()
            if row:
                grid.append(line.strip())
    return grid

def GetGridElement(grid, row, col):
    grid_row = grid[row]
    grid_col = grid_row[col % len(grid_row)]
    return grid_col

grid = ReadGrid(sys.argv[1])
grid_height = len(grid)
delta_row = 1
delta_col = 3

row = 0
col = 0
trees = 0
while row < grid_height:
    if GetGridElement(grid, row, col) == "#":
        trees += 1
    row += delta_row
    col += delta_col

print(trees)
