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

def ComputeTrees(grid, delta_row, delta_col):
    grid_height = len(grid)
    row = 0
    col = 0
    trees = 0
    while row < grid_height:
        if GetGridElement(grid, row, col) == "#":
            trees += 1
        row += delta_row
        col += delta_col
    return(trees)

grid = ReadGrid(sys.argv[1])

prod = 1
for delta_col,delta_row in [ (1,1), (3,1), (5,1), (7,1), (1, 2) ]:
    trees = ComputeTrees(grid, delta_row, delta_col)
    print("Slope {dc},{dr} encounters {trees} trees".format(dc=delta_col, dr=delta_row, trees=trees))
    prod *= trees

print(prod)
