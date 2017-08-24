import builtins
import time

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

from main import main
builtins.main = main

builtins.player = Player()

def Instructions():
    print("Blah blah blah")


def level_up():
print(
'''
#           #########   #         #   ##########   #                #        #  #########   #
#           #           #         #   #            #                #        #  #       #   #
#           #           #         #   #            #                #        #  #       #   #
#           ########     #       #    ##########   #                #        #  #########   #
#           #             #     #     #            #                #        #  #           #
#           #              #   #      #            #                #        #  #          
########    #########       ###       ##########   ##########       ##########  #           #
''')


