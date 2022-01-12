from os import system
system('py -m pip install multipledispatch')
system('py -m pip install PySide6')
system('py -m pip install PyQt5')

import sys
from PySide6.QtWidgets import QApplication, QLabel
import time
from cell import Cell
from play import Play
from board import Board

play = Play()
n = int(input())
for i in range(n):
   x, y = map(int, input().split())
   play.add_cell(x, y)
play.display()

for i in range(10):
   play.turn()
   play.display()
