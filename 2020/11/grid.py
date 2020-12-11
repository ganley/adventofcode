from collections import Counter
import copy


# class for dealing with grids of states
# hat tip to Matt Boehm for suggesting the dict of (x,y) tuples representation
class Grid:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.grid = {}

    # fill from a list of strings, each string a row
    def fill(self, list_of_str, empty_state=None):
        for row, row_str in enumerate(list_of_str):
            for col, col_state in enumerate(row_str):
                if col_state != empty_state:
                    self.grid[(col, row)] = col_state
        self.width = max([coord[0] for coord in self.grid]) + 1
        self.height = max([coord[1] for coord in self.grid]) + 1

    # read a representation from a file
    def read(self, f, empty_state=None):
        self.fill([line.strip() for line in f.readlines()], empty_state)

    # copy another Grid
    def copy(self, grid):
        self.width = grid.width
        self.height = grid.height
        self.grid = copy.deepcopy(grid.grid)

    # get the state of the cell at (x,y)
    def get(self, x, y, default=None):
        return self.grid.get((x, y), default)

    # set the state of the cell at (x,y)
    def set(self, x, y, v):
        self.grid[(x, y)] = v

    # test for equality against another Grid
    def __eq__(self, rhs):
        return rhs.width == self.width and rhs.height == self.height \
            and rhs.grid == self.grid

    # test for inequality against another Grid
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    # produce string representation suitable for printing
    def __str__(self, empty_char="."):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self.get(x, y) or empty_char
            s += "\n"
        return s[:-1]     # drop the last \n

    # eight compass directions
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

    # neighbors within given distance along each compass direction
    # only the first neighbor encountered in each direction is counted
    # specifying dist=0 means look all the way to the edges
    def neighbors(self, x, y, dist=1):
        if dist == 0:
            dist = self.height + self.width      # effectively infinity
        neigh = []
        for dx, dy in Grid.deltas:
            cx, cy = x + dx, y + dy
            for d in range(dist):
                if v := self.get(cx, cy):
                    neigh.append(v)
                    break
                cx += dx
                cy += dy
        return Counter(neigh)

    # count of cells with the given state
    def count(self, state):
        return len([v for k, v in self.grid.items() if v == state])
