from collections import Counter
import copy


# class for dealing with hexagonal grids of states
# this differs from the rectangular one only in the set of neighbors and
# the to_string routine
# hat tip to Matt Boehm for suggesting the dict of (x,y) tuples representation
class HexGrid:
    def __init__(self):
        self.grid = {}

    # copy another HexGrid
    def copy(self, grid):
        self.grid = copy.deepcopy(grid.grid)

    # get the state of the cell at (x,y)
    def get(self, x, y, default=None):
        return self.grid.get((x, y), default)

    # set the state of the cell at (x,y)
    def set(self, x, y, v):
        self.grid[(x, y)] = v

    # test for equality against another HexGrid
    def __eq__(self, rhs):
        return rhs.width == self.width and rhs.height == self.height \
            and rhs.grid == self.grid

    # test for inequality against another HexGrid
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    # produce string representation suitable for printing
    # the labeling of coordinates will behave very badly if they are more than
    # single digits
    def to_string(self, empty_char="w"):
        xs = [c[0] for c in self.grid.keys()] + [-1, 1]
        minx, maxx = min(xs), max(xs)
        ys = [c[1] for c in self.grid.keys()] + [-1, 1]
        miny, maxy = min(ys), max(ys)
        s = "   "
        for x in range(minx, maxx + 1):
            s += str(abs(x))
        s += "\n"
        compass = {(-1, 0): "<", (1, 0): ">", (0, -1): "^", (0, 1): "v"}
        for y in range(miny, maxy + 1):
            if y < 0:
                s += str(y) + " "
            else:
                s += " " + str(y) + " "
            for x in range(minx, maxx + 1):
                c = self.get(x, y)
                s += c if c else \
                     "W" if x % 2 == y % 2 else compass.get((x, y), empty_char)
            s += "\n"
        return s[:-1]     # drop the last \n

    # six hexagonal neighbors
    deltas = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]

    # neighbors along each hexagonal direction
    def neighbors(self, x, y, empty_state="w"):
        neigh = []
        for dx, dy in HexGrid.deltas:
            neigh.append(self.get(x + dx, y + dy, empty_state))
        return Counter(neigh)

    # count of cells with the given state
    def count(self, state):
        return len([v for k, v in self.grid.items() if v == state])
