import sys
from typing import List


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


def read_grid(filename: str):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            if row := line.strip():
                grid.append(row)
    return grid


def get_grid_element(grid: List[str], row: int, col: int):
    grid_row = grid[row]
    grid_col = grid_row[col % len(grid_row)]
    return grid_col


grid = read_grid(sys.argv[1])
grid_height = len(grid)
delta_row = 1
delta_col = 3

row, col = 0, 0
trees = 0
while row < grid_height:
    if get_grid_element(grid, row, col) == "#":
        trees += 1
    row += delta_row
    col += delta_col

print(trees)
