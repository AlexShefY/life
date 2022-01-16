from board import Board

class Play:
    board = Board()
    
    def turn(self):
        cells_to_delete = self.board.cells_to_delete()
        cells_to_add = self.board.cells_to_add()
        for cell in cells_to_delete:
            self.board.remove_cell(cell)
        for cell in cells_to_add:
            self.board.add_cell(cell)
    
    def add_cell(self, i, j):
        self.board.add_cell(i, j)
    
    def out_consol(self):
        self.board.out_consol()

    def plot(self):
        self.board.plot()
