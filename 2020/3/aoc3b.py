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



def read_grid(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            if row := line.strip():
                grid.append(line.strip())
    return grid



def get_grid_element(grid, row, col):
    grid_row = grid[row]
    grid_col = grid_row[col % len(grid_row)]
    return grid_col



def compute_trees(grid, delta_row, delta_col):
    grid_height = len(grid)
    row,col = 0,0
    trees = 0
    while row < grid_height:
        if get_grid_element(grid, row, col) == "#":
            trees += 1
        row += delta_row
        col += delta_col
    return(trees)



grid = read_grid(sys.argv[1])

prod = 1
for delta_col,delta_row in [ (1,1), (3,1), (5,1), (7,1), (1, 2) ]:
    trees = compute_trees(grid, delta_row, delta_col)
    print("Slope {dc},{dr} encounters {trees} trees".format(dc=delta_col, dr=delta_row, trees=trees))
    prod *= trees

print(prod)

