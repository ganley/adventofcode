from collections import Counter
import copy


# class for dealing with grids of states
class Grid:
    def __init__(self):
        self.grid = {}

    # fill z=0 from a list of strings, each string a row
    def fill(self, list_of_str, empty_state=None):
        for row, row_str in enumerate(list_of_str):
            for col, col_state in enumerate(row_str):
                if col_state != empty_state:
                    self.grid[(col, row, 0, 0)] = col_state

    # read a representation from a file
    def read(self, f, empty_state=None):
        self.fill([line.strip() for line in f.readlines()], empty_state)

    # copy another Grid
    def copy(self, grid):
        self.grid = copy.deepcopy(grid.grid)

    # get the state of the cell at (x,y,z,w)
    def get(self, x, y, z, w, default=None):
        return self.grid.get((x, y, z, w), default)

    # set the state of the cell at (x,y,z,w)
    def set(self, x, y, z, w, v):
        if v == ".":
            del self.grid[(x, y, z, w)]
        else:
            self.grid[(x, y, z, w)] = v

    # test for equality against another Grid
    def __eq__(self, rhs):
        return rhs.grid == self.grid

    # test for inequality against another Grid
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    # 80 compass directions
    deltas = [(-1, -1, -1, -1), (-1, -1, -1, 0), (-1, -1, -1, 1),
              (-1, -1, 0, -1), (-1, -1, 0, 0), (-1, -1, 0, 1), (-1, -1, 1, -1),
              (-1, -1, 1, 0), (-1, -1, 1, 1), (-1, 0, -1, -1), (-1, 0, -1, 0),
              (-1, 0, -1, 1), (-1, 0, 0, -1), (-1, 0, 0, 0), (-1, 0, 0, 1),
              (-1, 0, 1, -1), (-1, 0, 1, 0), (-1, 0, 1, 1), (-1, 1, -1, -1),
              (-1, 1, -1, 0), (-1, 1, -1, 1), (-1, 1, 0, -1), (-1, 1, 0, 0),
              (-1, 1, 0, 1), (-1, 1, 1, -1), (-1, 1, 1, 0), (-1, 1, 1, 1),
              (0, -1, -1, -1), (0, -1, -1, 0), (0, -1, -1, 1), (0, -1, 0, -1),
              (0, -1, 0, 0), (0, -1, 0, 1), (0, -1, 1, -1), (0, -1, 1, 0),
              (0, -1, 1, 1), (0, 0, -1, -1), (0, 0, -1, 0), (0, 0, -1, 1),
              (0, 0, 0, -1), (0, 0, 0, 1), (0, 0, 1, -1), (0, 0, 1, 0),
              (0, 0, 1, 1), (0, 1, -1, -1), (0, 1, -1, 0), (0, 1, -1, 1),
              (0, 1, 0, -1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, -1),
              (0, 1, 1, 0), (0, 1, 1, 1), (1, -1, -1, -1), (1, -1, -1, 0),
              (1, -1, -1, 1), (1, -1, 0, -1), (1, -1, 0, 0), (1, -1, 0, 1),
              (1, -1, 1, -1), (1, -1, 1, 0), (1, -1, 1, 1), (1, 0, -1, -1),
              (1, 0, -1, 0), (1, 0, -1, 1), (1, 0, 0, -1), (1, 0, 0, 0),
              (1, 0, 0, 1), (1, 0, 1, -1), (1, 0, 1, 0), (1, 0, 1, 1),
              (1, 1, -1, -1), (1, 1, -1, 0), (1, 1, -1, 1), (1, 1, 0, -1),
              (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, -1), (1, 1, 1, 0),
              (1, 1, 1, 1)]

    # neighbors along each compass direction
    def neighbors(self, x, y, z, w):
        neigh = []
        for dx, dy, dz, dw in Grid.deltas:
            cx, cy, cz, cw = x + dx, y + dy, z + dz, w + dw
            if v := self.get(cx, cy, cz, cw):
                neigh.append(v)
        return Counter(neigh)

    # count of cells with the given state
    def count(self, state):
        return len([v for k, v in self.grid.items() if v == state])
