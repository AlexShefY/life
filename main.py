from os import system
system('py -m pip install multipledispatch')

import time
from cell import Cell
from play import Play
from board import Board

play = Play()
print("Enter the number of taken cells:")
n = int(input())

print("Enter taken cells:")
for i in range(n):
   x, y = map(int, input().split())
   play.add_cell(x, y)

play.plot()

for i in range(10):
   play.turn()
   play.plot()
