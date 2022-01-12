
class Cell:
    x : int
    y : int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def check(self, board):
        coun = 0
        for cell in self.neighbours():
            if board.is_taken(cell.x, cell.y):
                coun += 1
        return coun < 2 or coun > 3

    def equiv(self, i, j):
        return self.x == i and self.y == j

    def neighbours(self):
        neighbours = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not i == 0 or not j == 0:
                    neighbours.add(Cell(self.x + i, self.y + j))
        return neighbours
