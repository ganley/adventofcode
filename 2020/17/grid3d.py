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
                    self.grid[(col, row, 0)] = col_state

    # read a representation from a file
    def read(self, f, empty_state=None):
        self.fill([line.strip() for line in f.readlines()], empty_state)

    # copy another Grid
    def copy(self, grid):
        self.grid = copy.deepcopy(grid.grid)

    # get the state of the cell at (x,y,z)
    def get(self, x, y, z, default=None):
        return self.grid.get((x, y, z), default)

    # set the state of the cell at (x,y,z)
    def set(self, x, y, z, v):
        if v == ".":
            del self.grid[(x, y, z)]
        else:
            self.grid[(x, y, z)] = v

    # test for equality against another Grid
    def __eq__(self, rhs):
        return rhs.grid == self.grid

    # test for inequality against another Grid
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    # produce string representation suitable for printing
    def one_plane_str(self, z, empty_char="."):
        xs = [coord[0] for coord in self.grid]
        minx, maxx = min(xs), max(xs)
        ys = [coord[1] for coord in self.grid]
        miny, maxy = min(ys), max(ys)
        s = ""
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                s += self.get(x, y, z) or empty_char
            s += "\n"
        return s[:-1]     # drop the last \n

    def __str__(self, empty_char="."):
        zs = [coord[2] for coord in self.grid]
        minz, maxz = min(zs), max(zs)
        s = ""
        for z in range(minz, maxz + 1):
            s += f"{z=}\n"
            s += self.one_plane_str(z, empty_char)
            s += "\n\n"
        return s[:-2]     # drop the last \n

    # 26 compass directions
    deltas = [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1),
              (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0), (-1, 1, 1),
              (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 1),
              (0, 1, -1), (0, 1, 0), (0, 1, 1), (1, -1, -1), (1, -1, 0),
              (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1),
              (1, 1, 0), (1, 1, 1)]

    # neighbors along each compass direction
    def neighbors(self, x, y, z):
        neigh = []
        for dx, dy, dz in Grid.deltas:
            cx, cy, cz = x + dx, y + dy, z + dz
            if v := self.get(cx, cy, cz):
                neigh.append(v)
        return Counter(neigh)

    # count of cells with the given state
    def count(self, state):
        return len([v for k, v in self.grid.items() if v == state])
