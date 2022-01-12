from os import system
system('py -m pip install multipledispatch')

import time
from cell import Cell
from play import Play
from board import Board

play = Play()
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    play.add_cell(x, y)
play.out()
for i in range(10):
    play.turn()
    play.out()
    time.sleep(1)
