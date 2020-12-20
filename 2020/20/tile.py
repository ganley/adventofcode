from collections import Counter
import copy


# class for dealing with grids of states
# hat tip to Matt Boehm for suggesting the dict of (x,y) tuples representation
class Tile:
    def __init__(self, txt="", empty_state=None):
        self.grid = {}
        if txt:
            self.fill(txt, empty_state)

    # fill from a list of strings, each string a row
    def fill(self, list_of_str, empty_state=None):
        assert list_of_str[0].startswith("Tile")
        self.id = int(list_of_str[0].split()[1][:-1])    # drop trailing :
        for row, row_str in enumerate(list_of_str[1:]):
            for col, col_state in enumerate(row_str):
                if col_state != empty_state:
                    self.grid[(col, row)] = col_state
        self.width = max([coord[0] for coord in self.grid]) + 1
        self.height = max([coord[1] for coord in self.grid]) + 1

    # read a representation from a file
    def read(self, f, empty_state=None):
        self.fill([line.strip() for line in f.readlines()], empty_state)

    # copy another Tile
    def copy(self, grid):
        self.id = grid.id
        self.width = grid.width
        self.height = grid.height
        self.grid = copy.deepcopy(grid.grid)

    def rotate(self):
        newtile = Tile()
        newtile.id = self.id
        newtile.width, newtile.height = self.height, self.width
        for coord, value in self.grid.items():
            newtile.set(coord[1], coord[0], value)
        return newtile

    def flipx(self):
        newtile = Tile()
        newtile.width, newtile.height = self.width, self.height
        newtile.id = self.id
        for coord, value in self.grid.items():
            newtile.set(self.width - coord[0] - 1, coord[1], value)
        return newtile

    def flipy(self):
        newtile = Tile()
        newtile.width, newtile.height = self.width, self.height
        newtile.id = self.id
        for coord, value in self.grid.items():
            newtile.set(coord[0], self.height - coord[1] - 1, value)
        return newtile

    def matches_right(self, right):
        for y in range(self.height):
            if self.get(self.width - 1, y, ".") != right.get(0, y, "."):
                return False
        return True

    def matches_down(self, down):
        for x in range(self.width):
            if self.get(x, self.height - 1, ".") != down.get(x, 0, "."):
                return False
        return True

    # get the state of the cell at (x,y)
    def get(self, x, y, default=None):
        return self.grid.get((x, y), default)

    # set the state of the cell at (x,y)
    def set(self, x, y, v):
        self.grid[(x, y)] = v

    # test for equality against another Tile
    def __eq__(self, rhs):
        return rhs.id == self.id and rhs.width == self.width and \
            rhs.height == self.height and rhs.grid == self.grid

    # test for inequality against another Tile
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    # produce string representation suitable for printing
    def __str__(self, empty_char="."):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self.get(x, y) or empty_char
            s += "\n"
        return f"Tile {self.id}:\n{s[:-1]}"     # drop the last \n
