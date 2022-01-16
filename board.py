from multipledispatch import dispatch
from cell import Cell
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
from matplotlib.artist import Artist

def close_event():
    plt.close() #timer calls this function after 3 seconds and closes the window 

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
    
    def out_consol(self):
        for x in range(10):
            for y in range(10):
                if self.is_taken(x, y):
                    print("*", end="")
                else:
                    print("_", end="")
            print()
        print()

    def plot(self):
        timer =  plt.figure().canvas.new_timer(interval = 3000)
        timer.add_callback(close_event)
        timer.start()
        ax = plt.subplot()
        polys = []
        minx = 1e9
        maxx = -1e9
        miny = 1e9
        maxy = -1e9
        
        for cell in self.cells:
            minx = min(minx, cell.x)
            miny = min(miny, cell.y)
            maxx = max(maxx, cell.x)
            maxy = max(maxy, cell.y)

        len_sq = max(maxy - miny, maxx - minx)
        maxx = minx + len_sq
        maxy = miny + len_sq

        for i in range(minx, maxx + 1):
            for j in range(miny, maxy + 1):
                xs = [i, i + 1, i + 1, i, i]
                ys = [j, j, j + 1, j + 1, j]
                color = 'b'
                if self.is_taken(i, j):
                    color = 'r'
                poly = Polygon(np.column_stack([xs, ys]), color=color)
                ax.add_patch(poly)

        ax.set_xlim((minx, maxx + 1))
        ax.set_ylim((miny, maxy + 1))

        for i in range(len_sq + 1):
            plt.plot([minx, maxx + 1], [miny + i, miny + i], marker='o', color='y')
            plt.plot([minx + i, minx + i], [miny, maxy + 1], marker='o', color='y')
        
        plt.show()

    def check(self, cell):
        coun = 0
        for cell_ in cell.neighbours():
            if self.is_taken(cell_.x, cell_.y):
                coun += 1
        return coun < 2 or coun > 3