import sys

import builtins
import time

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

from main import main,clear_screen
builtins.main = main
builtins.clear_screen = clear_screen

from generate_board import generate_board
builtins.generate_board = generate_board

builtins.level = 1
builtins.score = 0


def Instructions():
    print('''
    Welcome to bomberman!
    To move player, use a,s,d,w
    To drop bomb, use b
    To quit,press q
    
    You get 20 points for destroying walls
    And 100 points for destroying enemies
    
    Destroy all enemies to win!
    (Game starts in 10 seconds)
    ''')
    time.sleep(1)
    clear_screen()

def win():
    print("YOU WIN!")
    print("YOUR FINAL SCORE: ",score)
    sys.exit()


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
    time.sleep(3)
    clear_screen()
    
    global level
    level += 1

    global score
    score += player.score

    if level == 5:
        win()

    dimensions = [3 + level*2, 3 + level*2]
    level_board = generate_board(dimensions, level, 3*level)
    builtins.board = Board(level_board, dimensions)
    board.update_positions()

    while True:
        main()

builtins.level_up = level_up

#It all starts here!
def start():
    Instructions()
    dimensions = [3 + level*2, 3 + level*2]
    level_board = generate_board(dimensions, level, 3*level)
    builtins.board = Board(level_board ,dimensions)
    board.update_positions()

    while True:
        main()

start()


