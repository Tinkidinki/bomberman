import builtins

from input_char import getch
builtins.getch = getch

from board_object import Board_Object
builtins.Board_Object = Board_Object

from board import Board
builtins.Board = Board

from walls import Permanant_Wall, Brick_Wall
builtins.Permanant_Wall = Permanant_Wall
builtins.Brick_Wall = Brick_Wall

from bomb import Bomb
builtins.Bomb = Bomb

from player import Player
builtins.Player = Player

from enemy import Enemy
builtins.Enemy = Enemy

from nothing import Nothing
builtins.Nothing = Nothing

from main import each_frame, do_all_checks
builtins.each_frame = each_frame
builtins.do_all_checks = do_all_checks

builtins.player = Player()
builtins.enemy = Enemy()

#d
print(Nothing)
n = Nothing()
print(n)

#It might be useful to remove position argument completely for Nothing() and Permanant_Wall() objects
#Oh god, this is circular. How did it take me this long to figure.

level1_board = [[player, Permanant_Wall(),Nothing(),Brick_Wall()],
[Nothing(),Nothing(),enemy,Nothing()],
[Permanant_Wall(),Nothing(),Permanant_Wall(),Nothing()],
[Nothing(),Permanant_Wall(),Nothing(),Nothing()]]


dimensions = [4,4]

builtins.board = Board(level1_board,dimensions)

#d
for i in level1_board:
    for j in i:
        print (j.position,end = " ")
    print()

board.update_positions()

#d
for i in level1_board:
    for j in i:
        print (j.position, end=" ")
    print()

print(Permanant_Wall)
board.display()
each_frame()

