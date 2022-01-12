from multipledispatch import dispatch
from cell import Cell
from collections import namedtuple

class Board:
    cells = set()

    def is_taken(self, i, j):
        for cell in self.cells:
            if cell.equiv(i, j):
                return True
        return False

    def cells_to_add(self):
        cells_to_add = set()
        d = dict()
        for cell in self.cells:
            for neighbour in cell.neighbours():
                if not self.is_taken(neighbour.x, neighbour.y):
                    d[(neighbour.x, neighbour.y)] = d.get((neighbour.x, neighbour.y), 0) + 1
        for cell in d.keys():
            if d[cell] == 3:
                cells_to_add.add(Cell(cell[0], cell[1]))
        return cells_to_add
    
    def cells_to_delete(self):
        cells_to_delete = set()
        for cell in self.cells:
            if self.check(cell):
                cells_to_delete.add(cell)
        return cells_to_delete

    @dispatch(int, int)
    def add_cell(self, i, j):
        self.cells.add(Cell(i, j))

    @dispatch(Cell)
    def add_cell(self, cell):
        self.cells.add(cell)

    def remove_cell(self, cell):
        self.cells.remove(cell)
    
    def out(self):
        for x in range(10):
            for y in range(10):
                if self.is_taken(x, y):
                    print("*", end="")
                else:
                    print("_", end="")
            print()
        print()

    def check(self, cell):
        coun = 0
        for cell_ in cell.neighbours():
            if self.is_taken(cell_.x, cell_.y):
                coun += 1
        return coun < 2 or coun > 3