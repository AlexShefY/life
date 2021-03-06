
class Cell:
    x : int
    y : int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equiv(self, i, j):
        return self.x == i and self.y == j

    def neighbours(self):
        neighbours = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not i == 0 or not j == 0:
                    neighbours.add(Cell(self.x + i, self.y + j))
        return neighbours
